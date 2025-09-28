import os
import sys
import subprocess

# =========================
# CHECA E INSTALA DEPENDÊNCIAS
# =========================
def ensure_package(pkg):
    try:
        __import__(pkg)
    except ImportError:
        print(f"[INFO] Instalando pacote: {pkg}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

required = ["ultralytics", "cv2", "matplotlib", "requests"]
for pkg in required:
    pip_name = "opencv-python" if pkg == "cv2" else pkg
    try:
        __import__(pkg if pkg != "cv2" else "cv2")
    except ImportError:
        print(f"[INFO] Instalando {pip_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])

import time, csv
from datetime import datetime
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
import requests

MODEL_WEIGHTS = "yolov8n.pt"
CONF_THRESH = 0.5
CSV_PATH = "deteccoes.csv"
API_POST_URL = None

def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def ensure_csv(path):
    new = not os.path.exists(path)
    f = open(path, "a", newline="", encoding="utf-8")
    writer = csv.writer(f)
    if new:
        writer.writerow(["timestamp", "label", "conf", "x1", "y1", "x2", "y2", "cx", "cy", "evento"])
    return f, writer

model = YOLO(MODEL_WEIGHTS)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erro ao acessar a câmera.")
    sys.exit(1)

csv_file, csv_writer = ensure_csv(CSV_PATH)
points = []
W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
GATE_X = W // 2

print("Detecção de motos em tempo real (pressione 'e' para sair)")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame, verbose=False)[0]
        for box in results.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            conf = float(box.conf[0])
            if label.lower() in ["motorbike", "motorcycle"] and conf > CONF_THRESH:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                evento = "moto_esquerda" if cx < GATE_X else "moto_direita"
                csv_writer.writerow([now_str(), label, f"{conf:.2f}", x1, y1, x2, y2, cx, cy, evento])
                csv_file.flush()
                if API_POST_URL:
                    try:
                        requests.post(API_POST_URL, json={
                            "timestamp": now_str(),
                            "label": label,
                            "confianca": conf,
                            "evento": evento,
                            "coordenadas": {"x": cx, "y": cy}
                        }, timeout=2)
                    except Exception as e:
                        print(f"[WARN] Falha ao enviar para API: {e}")
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 255), 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 200, 255), 2)
                cv2.circle(frame, (cx, cy), 3, (0, 200, 255), -1)
                points.append((cx, cy))
        cv2.line(frame, (GATE_X, 0), (GATE_X, H), (255, 255, 255), 2)
        cv2.imshow("Deteccao de Motos", frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
    csv_file.close()

if points:
    plt.figure(figsize=(8, 5))
    plt.title("Pontos de Detecção de Motos")
    plt.xlabel("Largura")
    plt.ylabel("Altura")
    plt.gca().invert_yaxis()
    for x, y in points:
        plt.plot(x, y, 'ro', markersize=4)
    plt.axvline(x=GATE_X, linestyle="--", color="blue")
    plt.grid(True)
    plt.show()
