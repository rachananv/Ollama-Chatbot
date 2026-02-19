"""
Test script to verify Ollama connection and chatbot functionality.
This script checks if Ollama is running and attempts a simple connection.
"""

import requests
import sys
from typing import Tuple


def test_ollama_connection(url: str = "http://localhost:11434") -> Tuple[bool, str]:
    """Test if Ollama is running and accessible."""
    try:
        response = requests.get(f"{url}/api/tags", timeout=5)
        if response.status_code == 200:
            data = response.json()
            models = data.get('models', [])
            return True, f"Connected! Available models: {len(models)}"
        else:
            return False, f"Ollama returned status {response.status_code}"
    except requests.exceptions.ConnectionError:
        return False, "Cannot connect - Ollama may not be running"
    except Exception as e:
        return False, f"Error: {e}"


def get_available_models(url: str = "http://localhost:11434") -> list:
    """Get list of available models."""
    try:
        response = requests.get(f"{url}/api/tags", timeout=5)
        if response.status_code == 200:
            data = response.json()
            models = [model['name'] for model in data.get('models', [])]
            return models
    except:
        pass
    return []


def test_generation(prompt: str, model: str = "llama2") -> Tuple[bool, str]:
    """Test generation with a simple prompt."""
    try:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "temperature": 0.7,
        }
        
        print(f"Sending test prompt: '{prompt}'")
        print("Waiting for response (this may take a minute)...\n")
        
        response = requests.post(url, json=payload, timeout=300)
        
        if response.status_code == 200:
            result = response.json()
            generated = result.get('response', '').strip()
            return True, generated
        else:
            return False, f"Status code: {response.status_code}"
    except requests.exceptions.Timeout:
        return False, "Request timed out"
    except Exception as e:
        return False, str(e)


def main():
    """Run tests."""
    print("=" * 60)
    print("Ollama Chatbot - Diagnostic Test")
    print("=" * 60)
    
    # Test connection
    print("\n1. Testing Ollama Connection...")
    print("-" * 60)
    connected, msg = test_ollama_connection()
    print(msg)
    
    if not connected:
        print("\n❌ Ollama is not running!")
        print("\nTo start Ollama:")
        print("1. Download from https://ollama.ai/")
        print("2. Install and start Ollama")
        print("3. Run: ollama serve")
        print("\nTo pull a model:")
        print("4. Run: ollama pull llama2")
        return
    
    # Get available models
    print("\n2. Available Models:")
    print("-" * 60)
    models = get_available_models()
    if models:
        for model in models:
            print(f"  ✓ {model}")
    else:
        print("  No models found. Run: ollama pull llama2")
        return
    
    # Test generation
    print("\n3. Testing Generation (Simple Prompt):")
    print("-" * 60)
    success, result = test_generation("What is 2+2?", models[0])
    
    if success:
        print(f"✅ Generation successful!\n")
        print(f"Prompt: What is 2+2?")
        print(f"Response: {result}")
    else:
        print(f"❌ Generation failed: {result}")
    
    # Test with full chatbot
    print("\n" + "=" * 60)
    print("✅ Ready to use the chatbot!")
    print("=" * 60)
    print("\nTo start the interactive chatbot, run:")
    print("  python ollama_chatbot.py")
    print("\nOr use the simple example:")
    print("  python simple_example.py")


if __name__ == "__main__":
    main()
