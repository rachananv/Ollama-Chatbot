"""
Flask Web Chatbot - Cloud Deployment Version
Uses Groq API (free) instead of local Ollama
Get free API key from: https://console.groq.com/
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from groq import Groq

app = Flask(__name__)
CORS(app)

# Get Groq API key from environment variable
GROQ_API_KEY = os.getenv('GROQ_API_KEY', 'YOUR_GROQ_API_KEY_HERE')
client = Groq(api_key=GROQ_API_KEY)

MODEL = "mixtral-8x7b-32768"  # Free model from Groq
chat_history = []


@app.route('/')
def home():
    """Render the chat page."""
    return render_template('index.html', model=f"Groq {MODEL}")


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests."""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        # Call Groq API
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=1024,
        )
        
        bot_message = response.choices[0].message.content.strip()
        
        # Store in history
        chat_history.append({
            'user': user_message,
            'bot': bot_message
        })
        
        return jsonify({
            'success': True,
            'message': bot_message
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/models', methods=['GET'])
def get_models():
    """Get available models."""
    return jsonify({'models': [MODEL]})


@app.route('/api/health', methods=['GET'])
def health():
    """Check if API is working."""
    try:
        # Test API connection
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": "Hi"}],
            max_tokens=10,
        )
        return jsonify({
            'status': 'ok',
            'api_working': True
        })
    except:
        return jsonify({
            'status': 'error',
            'api_working': False
        })


@app.route('/api/history', methods=['GET'])
def get_history():
    """Get chat history."""
    return jsonify({'history': chat_history})


@app.route('/api/clear', methods=['POST'])
def clear_history():
    """Clear chat history."""
    global chat_history
    chat_history = []
    return jsonify({'success': True})


if __name__ == '__main__':
    print("=" * 60)
    print("Flask Groq Chatbot Starting...")
    print("=" * 60)
    print(f"\nModel: {MODEL}")
    print(f"API Key configured: {'Yes' if GROQ_API_KEY != 'YOUR_GROQ_API_KEY_HERE' else 'No'}")
    print("\nAccess at: http://localhost:5000/")
    print("=" * 60 + "\n")
    
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
