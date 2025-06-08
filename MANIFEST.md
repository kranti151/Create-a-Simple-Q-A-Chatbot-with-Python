# Terminal Chatbot Manifest

## Project Overview
This is a terminal-based chatbot built with Django and ChatterBot that allows users to have conversations with an AI bot through the command line interface.

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation Steps

1. **Clone the Repository**
```bash
git clone https://github.com/kranti151/Create-a-Simple-Q-A-Chatbot-with-Python/upload/main
cd terminalbot
```

2. **Create and Activate Virtual Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
pip install pyyaml
python -m spacy download en_core_web_sm
```

## Running the Application

1. **Start the Django Server**
```bash
# Make sure you're in the project directory
python manage.py runserver
```
The server will start at http://localhost:8000/

2. **Open a New Terminal Window**
Keep the Django server running in the first terminal window.

3. **Run the Terminal Client**
```bash
# In the new terminal window
python terminal_client.py
```

## Usage Instructions

1. Once the terminal client is running, you'll see a welcome message.
2. Type your message and press Enter to chat with the bot.
3. The bot will respond to your messages using its trained knowledge.
4. Type 'quit' to exit the chat.

## Example Interactions
```
You: Hello
Bot: Hi there! How are you doing?

You: What's your name?
Bot: I am Terminal Bot, nice to meet you!

You: Tell me a joke
Bot: Why don't scientists trust atoms? Because they make up everything!

You: quit
Bot: Goodbye!
```

## Troubleshooting

If you encounter any issues:

1. **Connection Error**
   - Make sure the Django server is running
   - Check if you're using the correct port (8000)

2. **Module Not Found Errors**
   - Ensure all dependencies are installed
   - Verify you're in the virtual environment

3. **ChatterBot Training Issues**
   - Make sure the spaCy model is installed
   - Check if the training data is properly loaded

## Project Structure
```
terminalbot/
├── chatbot_project/     # Django project settings
├── chat/               # Chat application
├── terminal_client.py  # Terminal interface
├── requirements.txt    # Project dependencies
├── MANIFEST.md        # This file
└── README.md          # Project overview
```
