🧠 Divina – Your Personal AI Assistant
Divina is a smart, friendly, and file-aware chatbot powered by Google's Gemini AI, built using Flask and enhanced with a responsive JavaScript frontend. This assistant can read images and PDFs, respond in Markdown, accept voice input, and even request feedback—all designed with a personal touch by Divine Mathem.

🚀 Features
🧾 Chat with PDF and Image Understanding

🎤 Voice Input via Web Speech API

💬 Markdown-formatted, friendly AI replies

📁 File previews with real-time user feedback

🗣️ Speech synthesis to read AI responses aloud

💾 Conversation history and session management

🌍 CORS-enabled Flask API

🗂️ Project Structure
bash
Copy
Edit
📦 divina-chatbot/
├── app.py                 # Backend Flask app with Gemini integration
├── templates/             # (Optional) HTML frontend if using server-side rendering
├── static/                # Your JS/CSS/images for the chatbot frontend
│   └── chatbot.js         # Responsive frontend logic
├── .env                   # Environment file storing GEMINI_API_KEY
├── requirements.txt       # Python package dependencies
├── README.md              # Project overview (this file)
└── index.txt              # Internal notes or system prompt config (if used)
🧠 Assistant Personality
“Hi, I'm Divina, your personal AI assistant built by Divine Mathem. I'm always happy to help, and I try to keep my answers clear, kind, and useful. If you'd like, you can give Divine feedback on how I'm doing! 😊”

System Behavior:
Keeps responses short and clear for long/complex prompts

Always follows a warm and professional tone

Provides structured answers (bullets, markdown, formatting)

Politely asks for user feedback (mentioning Divine's name)

⚙️ Setup Instructions
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/your-username/divina-chatbot.git
cd divina-chatbot
2. Create a virtual environment and activate it
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Create a .env file with your Gemini API key
env
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key_here
Don't share this key publicly!

5. Run the Flask backend
bash
Copy
Edit
python app.py
The API will run locally at: http://127.0.0.1:5000/api/DivineChat-AI

🧪 API Endpoints
POST /api/DivineChat-AI: Accepts text, PDF, or image input and returns AI-generated response

GET /api/health: Simple health check for the server

💻 Frontend Overview
The frontend uses plain JavaScript with a modern, chat-like UI:

Handles file preview for images and PDFs

Supports voice input and playback

Provides real-time message rendering with typing animation

Built to be mobile responsive and modular

📦 Dependencies (Python)
Listed in requirements.txt:

nginx
Copy
Edit
flask
flask-cors
google-generativeai
pymupdf
pillow
python-dotenv
👤 About the Creator
Divine Mathem is a BIT (Business Information Technology) student at the University of Johannesburg, originally from Kinshasa, DRC. He’s passionate about technology, creativity, and AI innovation.

📄 License
This project is licensed under the MIT License.
