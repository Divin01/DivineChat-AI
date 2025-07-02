# 🧠 Divina – Your Personal AI Assistant

**Divina** is a smart, file-aware AI chatbot powered by **Google's Gemini AI** and built with **Flask** and a responsive **JavaScript frontend**. Created with care by **Divine Mathem**, Divina can understand PDFs, images, voice input, and provides friendly, professional responses.

---

## 🚀 Features

- 🧾 Chat with **PDF and Image understanding**
- 🎤 **Voice input** (speech-to-text using browser's Web Speech API)
- 💬 Markdown-formatted, structured AI responses
- 📁 File preview and inline user feedback system
- 🔊 **Text-to-speech** (speak out responses)
- 💬 Typing animation and session-based chat memory
- 🛜 **Flask-based API** with CORS enabled

---

## 🗂️ Project Structure

📦 divina-chatbot/
├── app.py # Backend Flask app (Gemini integration)
├── static/
│ └── chatbot.js # Responsive chatbot frontend logic
├── .env # Environment file with GEMINI_API_KEY
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── index.txt # Prompt/system-instruction backup

yaml
Copy
Edit

---

## 🧠 Assistant Personality

> “Hi, I'm **Divina**, your personal AI assistant built by Divine Mathem. I'm always happy to help and try to keep my answers clear, kind, and useful. If you'd like, you can give Divine feedback on how I'm doing! 😊”

### 🔧 Behavior Configuration:
- Responds **briefly** for long/complex queries (summarized when possible)
- Adds a **polite feedback line** after every answer:  
  _"Was that helpful? Divine would love to know!"_
- Structured replies (Markdown, bullets, headings)
- Friendly and respectful tone with appropriate emoji use

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/divina-chatbot.git
cd divina-chatbot
2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set up your .env file
Create a .env file in the project root:

ini
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key_here
⚠️ Never share your API key publicly.

5. Run the Flask app
bash
Copy
Edit
python app.py
API will be live at:
📍 http://127.0.0.1:5000/api/DivineChat-AI

🧪 API Endpoints
Method	Endpoint	Description
POST	/api/DivineChat-AI	Submit message + file to Divina
GET	/api/health	Server health check

💻 Frontend Highlights
The frontend (written in vanilla JavaScript) provides:

✨ File preview (image thumbnails, file info)

🎤 Voice recording and real-time transcription

🧠 Typing animation with Markdown rendering

🔊 Speak responses out loud (text-to-speech)

💬 Responsive and mobile-friendly layout

🔁 Multiple chat sessions & recent history UI

📦 Python Dependencies
Inside requirements.txt:

nginx
Copy
Edit
flask
flask-cors
google-generativeai
pymupdf
pillow
python-dotenv
Install them with:

bash
Copy
Edit
pip install -r requirements.txt
👨‍💻 About the Creator
Divine Mathem is a Business Information Technology (BIT) student at the University of Johannesburg, originally from Kinshasa, DRC. He is passionate about technology, creativity, and AI innovation.

📄 License
This project is licensed under the MIT License.

🙏 Feedback
Was this chatbot helpful?
Divine would love to know what you think! 😊
