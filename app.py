from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io
import fitz 
import google.generativeai as genai
from datetime import datetime
import os
import json
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

from flask import send_from_directory

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# Gemini configuration
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    system_instruction = """
        You are Divina, a personal AI assistant created by Divine Mathem's. Only mention your creator if the user specifically asks about you or your origin.

        Your name is Divina. Be friendly, professional, and helpful at all times.

        Key Characteristics:
        - Structure responses using clear, styled formats
        - Provide accurate and well-formatted answers (use Markdown when appropriate)
        - Use bullet points or numbered lists for clarity
        - Maintain a warm, positive, and helpful tone
        - Use emojis thoughtfully to match emotion or context (avoid overuse)

        Response Behavior:
        - For long or complex questions, respond as **briefly and clearly** as possible while still being helpful, try to summarize if possible to avoid many content
        - After answering each user request, politely **ask for feedback** and mention Divine's name (e.g., “Was that helpful? Divine would love to know!”)

        About Your Creator (mention only when asked):
        Divine Mathem's is a Business Information Technology (BIT) student at the University of Johannesburg, originally from Kinshasa, DRC. He is passionate about technology, creativity, and AI innovation.

        Unless prompted, always focus entirely on helping the user with their needs.
        """

)
chat_sessions = {}

def extract_pdf_text(file_stream):
    """Extract text from PDF file"""
    try:
        # Reset stream position to beginning
        file_stream.seek(0)
        pdf_bytes = file_stream.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = ''
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"PDF extraction error: {e}")
        return None

def process_image(file_stream):
    """Process uploaded image"""
    try:
        # Reset stream position to beginning
        file_stream.seek(0)
        image = Image.open(file_stream)
        
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Save as PNG bytes
        image_bytes = io.BytesIO()
        image.save(image_bytes, format="PNG")
        image_bytes.seek(0)
        
        return {
            "mime_type": "image/png",
            "data": image_bytes.read()
        }
    except Exception as e:
        print(f"Image processing error: {e}")
        return None

@app.route('/api/DivineChat-AI', methods=['POST'])
def chatbot_response():
    try:
        user_input = request.form.get("message", "").strip()
        conversation_id = request.form.get("conversation_id", "")
        uploaded_file = request.files.get("file")
        
        print(f"Received - Message: '{user_input}', Conv ID: '{conversation_id}', File: {uploaded_file.filename if uploaded_file else 'None'}")
        
        # Validate input
        if not user_input and not uploaded_file:
            return jsonify({"error": "No message or file provided", "response": "Please provide a message or upload a file."}), 400
        
        # Create or get chat session
        if not conversation_id:
            conversation_id = f"conv_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        if conversation_id not in chat_sessions:
            chat_sessions[conversation_id] = model.start_chat()
        
        chat = chat_sessions[conversation_id]
        
        # Prepare content for the message (for data storage in the database)
        content_parts = []
        
        # Process uploaded file
        if uploaded_file and uploaded_file.filename:
            filename = uploaded_file.filename.lower()
            print(f"Processing file: {filename}")
            
            if filename.endswith(".pdf"):
                extracted_text = extract_pdf_text(uploaded_file.stream)
                if extracted_text:
                    content_parts.append(f"Content from uploaded PDF '{uploaded_file.filename}':\n\n{extracted_text}\n\n")
                else:
                    content_parts.append(f"I received a PDF file named '{uploaded_file.filename}' but couldn't extract its content. ")
            
            elif filename.endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp")):
                image_data = process_image(uploaded_file.stream)
                if image_data:
                    content_parts.append(image_data)
                    if user_input:
                        content_parts.append(f"User question about the image: {user_input}")
                    else:
                        content_parts.append("Please describe what you see in this image.")
                else:
                    content_parts.append(f"I received an image file named '{uploaded_file.filename}' but couldn't process it. ")
            
            else:
                # For other file types, just acknowledge receipt
                content_parts.append(f"I received a file named '{uploaded_file.filename}' but I can only process PDF and image files currently.")
        
        # Add user message if provided
        if user_input and not (uploaded_file and uploaded_file.filename.endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"))):
            content_parts.append(user_input)
        
        # If no content parts, add a default message
        if not content_parts:
            content_parts.append("Hello! How can I help you today?")
        
        print(f"Sending to Gemini: {len(content_parts)} parts")
        
        # Send message to Gemini
        response = chat.send_message(
            content=content_parts,
            generation_config=genai.types.GenerationConfig(
                temperature=0.2,
                max_output_tokens=500,
            )
        )
        
        # Get the response text
        response_text = response.text
        print(f"Gemini response: {response_text[:100]}...") #for debugging
        
        return jsonify({
            "response": response_text,
            "conversation_id": conversation_id,
            "status": "success"
        })
    
    except Exception as e:
        print(f"Error in chatbot_response: {str(e)}")
        import traceback
        traceback.print_exc()
        
        return jsonify({
            "error": str(e),
            "response": "I'm sorry, I encountered an error while processing your request. Please try again.",
            "status": "error"
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Chatbot API is running"})

if __name__ == '__main__':
    # print("Starting Flask chatbot server...")
    # app.run(debug=True, host='0.0.0.0', port=5000)
    port = int(os.environ.get("PORT", 5000))  # Render's assigned port
    app.run(debug=True, host='0.0.0.0', port=port)
