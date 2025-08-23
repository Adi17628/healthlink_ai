# 🏥 HealthLink AI – Your Personal AI Health Assistant  

HealthLink AI is an **AI-powered healthcare assistant** designed to provide **symptom guidance, first-aid tips, and medicine information** in a simple, structured, and user-friendly way.  
Built with **Streamlit** and powered by **Google Gemini API**, HealthLink AI helps users get **instant, reliable health information** while emphasizing the importance of consulting medical professionals.  

---

### Demo  
👉 [Live Demo on Hugging Face Spaces](https://huggingface.co/spaces/Adi222111/healthlink_ai)  

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Setup & Usage](#-setup--usage)
- [Disclaimer](#-disclaimer)

---

## 🌟 Overview  

HealthLink AI enables users to:  
- Get **first-aid recommendations** for symptoms.  
- Receive **home-care advice** and timelines for recovery.  
- Learn about **medicines** – their uses, side effects, and precautions.  
- Upload **medical images** (like rashes, wounds, or conditions) for AI-powered analysis.  

The system ensures responses are:  
- Written in **simple English (6th-grade level)**.  
- Limited to **150–200 words** for clarity.  
- Structured with **bullet points & emojis** for easy readability.  

---

## ✨ Features  

- **💬 Text Query Mode** – Ask about symptoms or medicines.  
- **📸 Image Analysis Mode** – Upload medical images for AI-based insights.  
- **⚠️ Safety Guardrails** – Clear emergency alerts and disclaimers.  
- **🎨 Beautiful UI** – Gradient headers, feature cards, and styled response containers.  

---

## 🏗️ Architecture  

### Basic Flow
1. User provides a **text query or image**.  
2. Request is processed via **Google Gemini API** with a structured **system prompt**.  
3. AI generates a **safe, structured response** (symptom guidance or medicine info).  
4. Streamlit displays results with **styled containers** and **disclaimer boxes**.  

---

## 📁 Project Structure  
```
healthlink_ai/ 
├── README.md 
├── REPORT.md  
├── CHANGELOG.md              
├── CONTRIBUTING.md           
├── LICENSE    
├── health.py 
├── requirements.txt
```

---

## ⚙️ Tech Stack  

- **Streamlit** → Front-end web app  
- **Google Gemini API** → AI model for text & image understanding  
- **PIL (Pillow)** → Image processing  
- **Python (Tempfile, IO, OS)** → File handling for image uploads  

---

## 🚀 Setup & Usage  

1. Clone the repository  
```bash
git clone https://code.swecha.org/adityaannamdevula/healthlink_ai

cd healthlink-ai
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the app
```bash
streamlit run health.py
```