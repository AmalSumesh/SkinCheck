# 🧠 SkinCheck – AI-Powered Skin Cancer Detection

An end-to-end intelligent system for **skin lesion classification and explainable AI-driven diagnosis**, combining deep learning, Grad-CAM visualization, and LLM-generated insights in a full-stack web application.

## 🚀 Demo

🎥 **Live Demo Video**  
https://github.com/user-attachments/assets/476f416e-a1a3-4c74-a1e-a1e1-f737a38a68e5

---
## 📌 Overview

**SkinCheck** is a full-stack AI application that classifies skin lesions as **benign or malignant** using a CNN model, enhances interpretability through **Grad-CAM heatmaps**, and generates **context-aware medical explanations** using an LLM.

The system focuses on making AI predictions **transparent, interpretable, and user-friendly**.

---

## ✨ Features

- 🧬 **Accurate Classification**
  - CNN model trained using TensorFlow
  - Outputs **Benign / Malignant** with confidence scores  

- 🔥 **Grad-CAM Explainability**
  - Visual heatmaps showing **key regions influencing predictions**

- 🤖 **LLM-Based Diagnostic Insights**
  - Converts model outputs into **human-readable explanations**

- 🌐 **Full-Stack Integration**
  - React frontend for seamless UX  
  - Flask backend serving ML inference  

- ⚡ **Real-Time Pipeline**
  - Upload → Predict → Visualize → Explain  

- 🌍 **Externally Accessible ML API**
  - Flask model served via **Ngrok for testing and external access**

---

## 🏗️ Tech Stack

**Frontend**
- React.js  
- HTML, CSS, JavaScript  

**Backend**
- Flask (Python)  
- REST API  

**Machine Learning**
- TensorFlow / Keras (CNN)  
- Grad-CAM  

**AI Integration**
- LLM for explanation generation  

**Deployment**
- Frontend: Vercel  
- Backend/ML: Render  
- API Exposure: Ngrok  

---

## 🧠 System Workflow

1. User uploads a skin lesion image  
2. Backend processes the image  
3. CNN model predicts:
   - **Benign / Malignant**
   - Confidence score  
4. Grad-CAM generates a **heatmap overlay**  
5. LLM generates a **diagnostic explanation**  
6. Results are displayed on the UI  

---

## 📂 Project Structure
