# Detecção de Motos com YOLOv8 — Sprint 3 (Disruptive Architectures)

## 📌 Descrição
Protótipo de visão computacional que detecta motos em tempo real usando YOLOv8.  
Atende aos requisitos da Sprint 3 (Disruptive Architectures: IoT, IOB & Generative IA).

- Output visual em tempo real
- Persistência em CSV
- Eventos (moto esquerda/direita do pátio)
- Integração opcional com backend
- Dashboard final com pontos detectados

## ⚙️ Requisitos
- Python 3.8+
- Webcam

## 📦 Instalação
Dependências são instaladas automaticamente ao rodar o script.  
Manual:
```bash
pip install ultralytics opencv-python matplotlib requests
```

## ▶️ Execução
```bash
python detectar_motos.py
```
Pressione **e** para sair.

## 📂 Saídas
- Arquivo `deteccoes.csv` com timestamp, label, confiança, coordenadas e evento.
- Janela com bounding boxes e linha virtual (gate).
- Gráfico final com pontos de detecção.

## 🌐 Integração com Backend
Defina no código:
```python
API_POST_URL = "http://localhost:8080/api/deteccoes"
```

## 🎥 Entregáveis
- Repositório GitHub com código + README + CSV
- Vídeo no YouTube demonstrando o funcionamento
