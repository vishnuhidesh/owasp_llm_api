from django.shortcuts import render
from random import choice
from time import sleep
from langchain_ollama import OllamaLLM
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .dependencies import system_prompt_leakage, prompt_rewriting_responses

model = OllamaLLM(model="llama3")



@api_view(['POST'])
def llm07(request):
    # change = False
    query = request.data.get('query', '').strip()

    # Initialize 'change' in the session if not already set
    if 'change' not in request.session:
        request.session['change'] = False

    # Check the value of 'change' from the session
    change = request.session['change']

    if query not in system_prompt_leakage or not change:
        if query in prompt_rewriting_responses:
            request.session['change'] = True  # Update session value
            sleep(2)
            result = prompt_rewriting_responses[query]
            return Response({'message': result})
        else:
            result = model.invoke(input=query)
            return Response({'message': result})

    elif change:
        result = system_prompt_leakage[query]
        sleep(3)
        return Response({'message': result})
