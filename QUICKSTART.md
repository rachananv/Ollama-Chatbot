# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Ollama
Download from https://ollama.ai/ and install on your system.

### Step 2: Pull a Model
Open terminal/command prompt and run:
```bash
ollama pull llama2
```

### Step 3: Start Ollama Server
Keep this running in the background:
```bash
ollama serve
```

### Step 4: Install Python Dependencies
In your project folder:
```bash
pip install -r requirements.txt
```

### Step 5: Run the Chatbot
Choose one:

**Interactive Chatbot (Full Features):**
```bash
python ollama_chatbot.py
```

**Simple Chatbot:**
```bash
python simple_example.py
```

**Diagnostic Test:**
```bash
python test_ollama.py
```

## 💡 Quick Commands

Inside the chatbot:
- Type your prompt and press Enter
- Type `history` to see past conversation
- Type `clear` to clear history
- Type `quit` or `exit` to exit

## 🎯 Example Usage

```python
# In simple_example.py or as a script:
from simple_example import chat_with_ollama

# Get a response
response = chat_with_ollama("Explain quantum computing in simple terms")
print(response)
```

## 🐛 Troubleshooting

**"Cannot connect to Ollama"**
→ Make sure `ollama serve` is running in another terminal

**"Model not found"**
→ Run `ollama pull llama2` (or your model name)

**Slow responses**
→ Try a faster model: `ollama pull neural-chat`

## 📚 Files Included

| File | Purpose |
|------|---------|
| `ollama_chatbot.py` | Full-featured chatbot class |
| `simple_example.py` | Minimal example |
| `test_ollama.py` | Verify everything works |
| `requirements.txt` | Python dependencies |
| `README.md` | Full documentation |

---

**That's it!** You now have a working Ollama chatbot. 🎉
