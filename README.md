# 🌸 Virtual Gynecologist Chatbot Assistant

A web-based chatbot assistant for Indian women, providing medically-informed, culturally sensitive, and supportive guidance on menstrual health, reproductive health, hormonal balance, hygiene, and emotional well-being.  
Powered by **Google Gemini AI (free version)** and built with **Flask**.

---

## ✨ Features

- 🩺 **Expert Guidance:**  
  Answers questions about menstrual, reproductive, hormonal, hygiene, and emotional health.
  
- 🌍 **Culturally Sensitive:**  
  Communicates using simple, respectful language appropriate to the Indian context.

- ✅ **Safe & Responsible:**  
  Never diagnoses or prescribes treatments. Refers users to doctors when necessary.

- 💬 **Modern Chat UI:**  
  Clean, responsive chat interface with supportive, empathetic tone.

- 🧠 **Session Memory:**  
  Remembers your conversation context during an active session.

---

## 📂 Project Structure

```
├── myenv/                # 🌱 Virtual environment (do not modify manually)
├── static/               # 🎨 Static files (CSS, JS, images)
├── templates/            # 🖼️ HTML templates (mainly for chat UI)
├── .env                  # 🔒 Environment variables (e.g., API keys)
├── app.py                # 🚀 Main Flask application
├── main.ipynb            # 🧪 Jupyter Notebook (for experiments or testing)
├── requirements.txt      # 📜 List of Python dependencies
└── README.md             # 📖 Project description (this file)
```

---

## 🛠️ Setup Instructions

1. **📥 Clone the repository**

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. **🌟 Create and activate a virtual environment**

```bash
python -m venv myenv
source myenv/bin/activate   # On Linux/macOS
myenv\Scripts\activate      # On Windows
```

3. **📦 Install required packages**

```bash
pip install -r requirements.txt
```

4. **🔧 Set up your `.env` file**

Create a `.env` file and add your API keys or configuration variables.  
Example:

```
SECRET_KEY=your_secret_key
GEMINI_API_KEY=your_gemini_api_key
```

5. **▶️ Run the Flask app**

```bash
python app.py
```

or

```bash
flask run
```

6. **🌐 Access the app**

Open your browser and go to:  
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python) 🐍
- **Frontend:** HTML, CSS 🎨
- **AI Engine:** Google Gemini API (free version) 🤖

---

## ⚠️ Disclaimer

This chatbot is intended for **informational purposes only**.  
It does **not** replace professional medical advice, diagnosis, or treatment.  
Always consult a qualified healthcare provider with any medical concerns.

---

## 📜 License

MIT License  
© 2025 [JeevanJyoti18](https://github.com/JeevanJyoti18)
