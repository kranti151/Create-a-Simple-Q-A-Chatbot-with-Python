# Terminal Chatbot

A simple terminal-based chatbot built with Django and ChatterBot.

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the chatbot:
```bash
python manage.py runserver
```

4. Open a new terminal and run:
```bash
python terminal_client.py
```

## Features
- Terminal-based chat interface
- Machine learning-based responses using ChatterBot
- Simple and intuitive user interaction

## Requirements
- Python 3.8+
- Django 4.2+
- ChatterBot 1.0.4+
- chatterbot-corpus 1.2.0+ 