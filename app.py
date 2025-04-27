from flask import Flask, render_template, request, session, redirect, url_for
from dotenv import load_dotenv
import os
import google.generativeai as genai
import markdown

# Load environment variables
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Configure Gemini API
genai.configure(api_key=os.getenv("api_key1"))

model = genai.GenerativeModel("gemini-2.0-flash")

SYSTEM_PROMPT = """You are a compassionate women's health advisor for Indian users. Follow these rules STRICTLY:

1. RESPONSE STRUCTURE:
   - Start with empathetic statement
   - Explain biological/medical context in simple terms
   - Suggest safe hygiene practices & lifestyle tips
   - Mention doctor only for severe/persistent symptoms

2. LANGUAGE:
   - Use simple English with Indian terms ("periods", "sanitary pad")
   - Culturally sensitive (avoid direct sex/contraception references)
   - 150-250 words, no markdown/emojis

3. NEVER:
   - Diagnose conditions
   - Prescribe medications
   - Give false assurances
   - Use casual language

Never break this format.

Example response format:
"I understand this can be worrying. Let me explain... [biological context]. You could try... [general advice]. If [specific condition] persists beyond [timeframe], consider consulting a gynecologist."
"""

PROHIBITED_PATTERNS = [
    "diagnos", "prescri", "medicine", "you should take", "tablet", "medication", "drug", "antibiotic"
]

def validate_response(text):
    # Check for prohibited patterns and length
    if any(term in text.lower() for term in PROHIBITED_PATTERNS):
        return False
    word_count = len(text.split())
    if word_count < 150 or word_count > 260:
        return False
    return True

def format_history():
    # Always start with system prompt for context
    history = [
        {'role': 'user', 'parts': [SYSTEM_PROMPT]},
        {'role': 'model', 'parts': ["Understood. I will follow all guidelines."]}
    ]
    # Add actual chat history
    history += [
        {'role': 'user' if r == 'You' else 'model', 'parts': [t]} 
        for r, t in session.get("chat_history", [])
    ]
    return history

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            # Prepare chat history for Gemini
            chat = model.start_chat(history=format_history())
            prompt = f"USER QUERY: {user_input}\n\nRemember to follow all guidelines and response structure."
            response = chat.send_message(prompt)
            # Retry if validation fails
            attempts = 0
            while not validate_response(response.text) and attempts < 2:
                response = model.generate_content(
                    f"Please rewrite the following to strictly follow the guidelines (no diagnosis, no prescriptions, 150-250 words, structure as instructed):\n\n{response.text}"
                )
                attempts += 1
            enhanced_response = markdown.markdown(response.text)
            session["chat_history"].extend([
                ("You", user_input),
                ("Bot", enhanced_response)
            ])
            session.modified = True

    return render_template(
        "index.html", 
        chat_history=session["chat_history"],
        response_text=session["chat_history"][-1][1] if session["chat_history"] else None
    )

@app.route("/reset")
def reset():
    session.pop("chat_history", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
