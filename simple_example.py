"""
Simple example of using Ollama to generate responses.
This is a minimal script to get started quickly.
"""

import requests

def chat_with_ollama(prompt: str, model: str = "llama3.2:latest") -> str:
    """
    Send a prompt to Ollama and get a response.
    
    Args:
        prompt: Your question or statement
        model: The Ollama model to use (default: llama3.2:latest)
    
    Returns:
        The generated response
    """
    try:
        url = "http://localhost:11434/api/generate"
        
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
        }
        
        print(f"Sending prompt to Ollama ({model})...")
        response = requests.post(url, json=payload, timeout=300)
        
        if response.status_code == 200:
            result = response.json()
            return result.get('response', '').strip()
        else:
            return f"Error: Ollama returned status {response.status_code}"
    
    except requests.exceptions.ConnectionError:
        return "Error: Cannot connect to Ollama. Make sure it's running on http://localhost:11434"
    except Exception as e:
        return f"Error: {e}"


def main():
    """Run simple chatbot example."""
    print("Ollama Chatbot - Simple Example")
    print("=" * 50)
    print("Make sure Ollama is running before starting!")
    print("Run: ollama serve")
    print("=" * 50)
    
    while True:
        prompt = input("\nYour prompt: ").strip()
        
        if not prompt:
            continue
        
        if prompt.lower() in ['quit', 'exit']:
            break
        
        response = chat_with_ollama(prompt)
        print(f"\nResponse:\n{response}")


if __name__ == "__main__":
    main()
