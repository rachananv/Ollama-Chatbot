"""
Ollama Chatbot - A simple chatbot that uses Ollama for generating responses.
Make sure Ollama is running on localhost:11434 before starting this script.

Install Ollama from: https://ollama.ai/
"""

import requests
import json
from typing import Optional

class OllamaChatbot:
    def __init__(self, model: str = "llama3.2:latest", ollama_url: str = "http://localhost:11434"):
        """
        Initialize the Ollama chatbot.
        
        Args:
            model: The Ollama model to use (e.g., 'llama3.2:latest', 'gemma3:4b', 'gpt-oss:120b-cloud')
            ollama_url: The URL where Ollama is running
        """
        self.model = model
        self.ollama_url = ollama_url
        self.api_endpoint = f"{ollama_url}/api/generate"
        self.chat_history = []
        
    def _check_connection(self) -> bool:
        """Check if Ollama is running and accessible."""
        try:
            response = requests.get(f"{self.ollama_url}/api/tags", timeout=5)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False
    
    def _get_available_models(self) -> list:
        """Get list of available models in Ollama."""
        try:
            response = requests.get(f"{self.ollama_url}/api/tags")
            if response.status_code == 200:
                data = response.json()
                models = [model['name'] for model in data.get('models', [])]
                return models
            return []
        except Exception as e:
            print(f"Error fetching models: {e}")
            return []
    
    def generate_response(self, prompt: str, temperature: float = 0.7) -> Optional[str]:
        """
        Generate a response from Ollama based on the given prompt.
        
        Args:
            prompt: The user's input prompt
            temperature: Controls randomness (0.0-1.0, higher = more random)
        
        Returns:
            The generated response as a string, or None if there's an error
        """
        try:
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "temperature": temperature,
            }
            
            response = requests.post(self.api_endpoint, json=payload, timeout=300)
            
            if response.status_code == 200:
                result = response.json()
                generated_text = result.get('response', '').strip()
                
                # Add to chat history
                self.chat_history.append({
                    "user": prompt,
                    "assistant": generated_text
                })
                
                return generated_text
            else:
                print(f"Error: Ollama returned status code {response.status_code}")
                return None
                
        except requests.exceptions.Timeout:
            print("Error: Request timed out. The model might be processing a long response.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to connect to Ollama. Make sure it's running on {self.ollama_url}")
            print(f"Details: {e}")
            return None
        except json.JSONDecodeError:
            print("Error: Failed to parse response from Ollama")
            return None
    
    def chat(self, prompt: str) -> Optional[str]:
        """
        Have a conversation with the chatbot.
        
        Args:
            prompt: The user's message
        
        Returns:
            The chatbot's response
        """
        return self.generate_response(prompt)
    
    def get_chat_history(self) -> list:
        """Get the conversation history."""
        return self.chat_history
    
    def clear_history(self):
        """Clear the conversation history."""
        self.chat_history = []


def main():
    """Main function to run the interactive chatbot."""
    
    print("=" * 60)
    print("Welcome to Ollama Chatbot!")
    print("=" * 60)
    
    # Initialize chatbot
    chatbot = OllamaChatbot(model="llama3.2:latest")
    
    # Check connection
    print(f"\nChecking connection to Ollama at http://localhost:11434...")
    if not chatbot._check_connection():
        print("❌ Error: Cannot connect to Ollama!")
        print("\nPlease make sure Ollama is running:")
        print("1. Download from: https://ollama.ai/")
        print("2. Install and start Ollama")
        print("3. Run: ollama pull llama2  (or your preferred model)")
        print("4. Run: ollama serve")
        return
    
    print("✅ Connected to Ollama!")
    
    # Show available models
    print(f"\nUsing model: {chatbot.model}")
    available_models = chatbot._get_available_models()
    if available_models:
        print(f"Available models: {', '.join(available_models)}")
    
    print("\nType 'quit' or 'exit' to stop the chatbot")
    print("Type 'clear' to clear conversation history")
    print("Type 'history' to see conversation history")
    print("-" * 60)
    
    # Interactive chat loop
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
            
            if user_input.lower() == 'clear':
                chatbot.clear_history()
                print("Conversation history cleared.")
                continue
            
            if user_input.lower() == 'history':
                history = chatbot.get_chat_history()
                if not history:
                    print("No conversation history yet.")
                else:
                    print("\n--- Conversation History ---")
                    for i, exchange in enumerate(history, 1):
                        print(f"\n[Exchange {i}]")
                        print(f"You: {exchange['user']}")
                        print(f"Bot: {exchange['assistant']}")
                continue
            
            print("\nBot: Thinking...", end="", flush=True)
            response = chatbot.chat(user_input)
            
            if response:
                print(f"\rBot: {response}")
            else:
                print("\rBot: Sorry, I couldn't generate a response. Please try again.")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            continue


if __name__ == "__main__":
    main()
