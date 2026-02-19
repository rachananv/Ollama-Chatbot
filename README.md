# Ollama Chatbot

A Python-based chatbot that uses Ollama for generating AI responses locally.

## Prerequisites

1. **Install Ollama**
   - Download from: https://ollama.ai/
   - Follow the installation instructions for your OS (Windows, Mac, or Linux)

2. **Pull a Model**
   - Open terminal/command prompt
   - Run: `ollama pull llama2` (or another model like `mistral`, `neural-chat`, etc.)

3. **Start Ollama Server**
   - Keep Ollama running in the background
   - Run: `ollama serve`
   - It will run on `http://localhost:11434`

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Chatbot

### Option 1: Full-Featured Chatbot (Recommended)
```bash
python ollama_chatbot.py
```

Features:
- Interactive conversation mode
- Command history
- Clear history option
- Error handling
- Connection checking

### Option 2: Simple Example
```bash
python simple_example.py
```

A minimal script for quick testing.

## Available Models

Popular Ollama models:
- `llama2` - Meta's LLaMA 2 (good general purpose)
- `mistral` - Mistral AI (faster, compact)
- `neural-chat` - Intel's Neural Chat (optimized)
- `dolphin-mixtral` - High-quality responses
- `orca-mini` - Lightweight model

To pull a model:
```bash
ollama pull mistral
ollama pull neural-chat
```

## Troubleshooting

### Issue: "Cannot connect to Ollama"
**Solution**: Make sure Ollama is running:
```bash
ollama serve
```

### Issue: Model not found
**Solution**: Pull the model first:
```bash
ollama pull llama2
```

### Issue: Response takes too long
**Solution**: 
- Try a smaller/lighter model (e.g., `neural-chat` instead of `llama2`)
- Adjust temperature parameter (lower = faster but less creative)
- Check your system resources

## Usage Examples

### Simple function call:
```python
from simple_example import chat_with_ollama

response = chat_with_ollama("What is Python?")
print(response)
```

### Using the full chatbot class:
```python
from ollama_chatbot import OllamaChatbot

chatbot = OllamaChatbot(model="mistral")
response = chatbot.chat("Hello, how are you?")
print(response)

# View history
history = chatbot.get_chat_history()
for exchange in history:
    print(f"User: {exchange['user']}")
    print(f"Bot: {exchange['assistant']}")
```

## Commands in Interactive Mode

- `quit` or `exit` - Exit the chatbot
- `clear` - Clear conversation history
- `history` - View conversation history
- Any text - Send as a prompt

## Performance Tips

1. **Use faster models** for quicker responses:
   - Try `neural-chat` or `mistral` instead of `llama2`

2. **Lower temperature** for faster, more deterministic responses:
   ```python
   chatbot.generate_response(prompt, temperature=0.3)
   ```

3. **Check system resources** - Ensure you have enough RAM and CPU available

## File Descriptions

- `ollama_chatbot.py` - Full-featured chatbot class with error handling
- `simple_example.py` - Minimal example for quick start
- `requirements.txt` - Python dependencies
- `README.md` - This file

## License

This code is provided as-is for educational purposes.

## References

- Ollama Official: https://ollama.ai/
- Available Models: https://ollama.ai/library
