from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import json

# Create your views here.

# Initialize the chatbot
chatbot = ChatBot('Terminal Bot')

# Train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.conversations")

@csrf_exempt
@require_http_methods(["POST"])
def chat(request):
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '')
        
        if not user_message:
            return JsonResponse({'error': 'No message provided'}, status=400)
        
        # Get response from chatbot
        bot_response = str(chatbot.get_response(user_message))
        
        return JsonResponse({'response': bot_response})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
