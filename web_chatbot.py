"""
Flask Web Chatbot - Access Ollama chatbot in your browser
Run this script and open: http://localhost:5000
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

OLLAMA_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3.2:latest"
chat_history = []


@app.route('/')
def home():
    """Render the chat page."""
    # Pass the active model to the template so the UI can display it
    return render_template('index.html', model=OLLAMA_MODEL)


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests."""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        # Call Ollama API
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": user_message,
                "stream": False,
                "temperature": 0.7,
            },
            timeout=300
        )
        
        if response.status_code == 200:
            result = response.json()
            bot_message = result.get('response', '').strip()
            
            # Store in history
            chat_history.append({
                'user': user_message,
                'bot': bot_message
            })
            
            return jsonify({
                'success': True,
                'message': bot_message
            })
        else:
            return jsonify({
                'success': False,
                'error': f'Ollama error: {response.status_code}'
            }), 500
    
    except requests.exceptions.Timeout:
        return jsonify({
            'success': False,
            'error': 'Request timed out - try a simpler question'
        }), 500
    except requests.exceptions.ConnectionError:
        return jsonify({
            'success': False,
            'error': 'Cannot connect to Ollama. Make sure it is running on localhost:11434'
        }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/models', methods=['GET'])
def get_models():
    """Get available Ollama models."""
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            data = response.json()
            models = [model['name'] for model in data.get('models', [])]
            return jsonify({'models': models})
        return jsonify({'models': []})
    except:
        return jsonify({'models': []})


@app.route('/api/health', methods=['GET'])
def health():
    """Check if Ollama is running."""
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        return jsonify({
            'status': 'ok' if response.status_code == 200 else 'error',
            'ollama_running': response.status_code == 200
        })
    except:
        return jsonify({
            'status': 'error',
            'ollama_running': False
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
    print("Flask Ollama Chatbot Starting...")
    print("=" * 60)
    print("\nOpen your browser at: http://localhost:5000")
    print("\nMake sure Ollama is running!")
    print("Run in another terminal: ollama serve")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 60 + "\n")
    
    app.run(debug=True, host='localhost', port=5000)
