<div align="center">

# 🤟 Sign Language Detection System

### AI-powered Real-Time Sign Language Recognition using YOLO & Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/YOLO-Ultralytics-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>

Real-time Sign Language Detection using Artificial Intelligence and Computer Vision.

</div>

---

# 📖 Overview

This project recognizes sign language gestures in real-time using a webcam. It utilizes a custom-trained YOLO model for object detection and converts recognized hand signs into readable text.

---

# ✨ Features

- 🎥 Real-time webcam detection
- 🤖 YOLO-based AI model
- 🖐️ Hand sign recognition
- ⚡ Fast inference
- 📝 Displays predicted alphabet
- 🔊 Optional text-to-speech
- 💻 Easy to train custom datasets

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| YOLO (Ultralytics) | Object Detection |
| OpenCV | Webcam Processing |
| PyTorch | Deep Learning |
| NumPy | Data Processing |

---

# 📂 Project Structure

```text
Sign-Language-Detection/
│
├── dataset/
│   ├── train/
│   ├── valid/
│   └── test/
│
├── models/
│   └── best.pt
│
├── runs/
│
├── detect.py
├── train.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Sign-Language-Detection.git

cd Sign-Language-Detection
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Detection

```bash
python detect.py
```

---

# 🧠 Train Model

```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=100 imgsz=640
```

---

# 📊 Dataset

The dataset contains labeled hand gesture images representing sign language alphabets.

Example folders

```text
A/
B/
C/
D/
...
Z/
```

---

# 📸 Demo

Add your screenshots here.

```
assets/demo.png
```

or

```
assets/demo.gif
```

---

# 📈 Future Improvements

- Sentence generation
- Voice output
- Mobile application
- Multiple hand detection
- Improved accuracy
- Continuous sign recognition

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

<div align="center">

### ⭐ Star this repository if you found it useful!

Made with ❤️ using Python & YOLO

</div>
