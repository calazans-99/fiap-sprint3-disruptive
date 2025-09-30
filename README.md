# 🏍️ Detector de Motos em Tempo Real  

Este projeto implementa um sistema de **detecção de motos em tempo real** utilizando **YOLOv8** da biblioteca [Ultralytics](https://docs.ultralytics.com/), com visualização via **OpenCV** e exportação de resultados para **CSV** (e opcionalmente envio para API).  

## ✨ Funcionalidades  

- Captura de vídeo em tempo real via webcam.  
- Detecção de motos (classes `motorbike` e `motorcycle`).  
- Salvamento das detecções em arquivo `deteccoes.csv` com:  
  - timestamp  
  - rótulo (label)  
  - confiança (conf)  
  - coordenadas (x1, y1, x2, y2)  
  - centroide (cx, cy)  
  - evento (`moto_esquerda` ou `moto_direita`) dependendo da posição relativa ao "gate".  
- Linha divisória central ("gate") para análise de fluxo.  
- Exibição gráfica dos pontos detectados em um scatter plot (matplotlib).  
- Integração opcional com **API REST** via `requests.post`.  

---

## 🛠️ Tecnologias Utilizadas  

- [Python 3.8+](https://www.python.org/)  
- [OpenCV](https://opencv.org/) (`cv2`)  
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)  
- [Matplotlib](https://matplotlib.org/)  
- [Requests](https://requests.readthedocs.io/)  

---

## 📦 Instalação  

Clone o repositório e instale as dependências:  

```bash
git clone https://github.com/seu-usuario/detector-motos.git
cd detector-motos

# Cria ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instala as dependências
pip install ultralytics opencv-python matplotlib requests
```

---

## ▶️ Uso  

Execute o script principal:  

```bash
python detectar_motos.py
```

### Teclas de controle  
- **`e`** → Encerra a captura de vídeo.  

---

## 📂 Estrutura dos Arquivos  

```
.
├── detectar_motos.py    # Script principal
├── deteccoes.csv        # Arquivo gerado com as detecções (criado na execução)
├── README.md            # Documentação
```

---

## ⚙️ Configuração  

No arquivo `detectar_motos.py`, você pode ajustar:  

- `MODEL_WEIGHTS`: modelo YOLOv8 usado (default: `yolov8n.pt`).  
- `CONF_THRESH`: limiar de confiança (default: `0.5`).  
- `CSV_PATH`: caminho para salvar os resultados (default: `deteccoes.csv`).  
- `API_POST_URL`: URL da API para envio das detecções (default: `None`).  

Exemplo para ativar envio de dados:  

```python
API_POST_URL = "http://localhost:5000/api/deteccoes"
```

---

## 📊 Saída  

### Tela de detecção  
- Retângulo em torno da moto detectada.  
- Label + confiança exibidos acima do retângulo.  
- Linha divisória no centro do vídeo.  

### Arquivo `deteccoes.csv`  
Exemplo de linha registrada:  

```csv
timestamp,label,conf,x1,y1,x2,y2,cx,cy,evento
2025-09-30 08:45:12,motorcycle,0.87,120,200,220,350,170,275,moto_esquerda
```

### Gráfico final  
- Scatter plot dos pontos detectados.  
- Linha divisória (`gate`) em azul tracejado.  

---

## 🚀 Próximos Passos  

- [ ] Implementar contagem de motos por lado (esquerda/direita).  
- [ ] Salvar imagens recortadas das detecções.  
- [ ] Dashboard em tempo real.  
- [ ] Deploy em Jetson Nano / Raspberry Pi.  

---

## 📜 Licença  

Este projeto é distribuído sob a licença MIT. Sinta-se à vontade para usar, modificar e compartilhar.  
