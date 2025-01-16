from django.shortcuts import render
from random import choice
from time import sleep
from langchain_ollama import OllamaLLM
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .dependency import instructions, error_responses

@api_view(['POST'])
def llm05(request):
    query = request.data.get('query','').strip()
    prompt = f"{instructions}\n\nQuery: {query}\nResponse:"
    model = OllamaLLM(model="llama3")
    flag = model.invoke(input=prompt)

    if flag == '1':
        result = choice(list(error_responses.values()))
        return Response({'message': result, 'flag': flag})
    
    else:
        result = model.invoke(input=query) 
        return Response({'message': result, 'flag': flag})


    