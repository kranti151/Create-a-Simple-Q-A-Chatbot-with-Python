import requests
import json

def chat_with_bot():
    print("Welcome to the Terminal Chatbot!")
    print("Type 'quit' to exit the chat.")
    print("-" * 50)
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
            
        try:
            # Send request to Django server
            response = requests.post(
                'http://localhost:8000/chat/',
                json={'message': user_input}
            )
            
            if response.status_code == 200:
                bot_response = response.json().get('response', 'Sorry, I did not understand that.')
                print(f"Bot: {bot_response}")
            else:
                print("Bot: Sorry, there was an error processing your request.")
                
        except requests.exceptions.ConnectionError:
            print("Bot: Unable to connect to the server. Please make sure the Django server is running.")
            break
        except Exception as e:
            print(f"Bot: An error occurred: {str(e)}")
            break

if __name__ == "__main__":
    chat_with_bot() 