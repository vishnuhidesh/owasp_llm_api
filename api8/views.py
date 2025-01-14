from django.shortcuts import render
from random import choice
from time import sleep
from langchain_ollama import OllamaLLM
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .instructions import instructions

model = OllamaLLM(model="llama3")



@api_view(['POST'])
def llm08(request):
    query1 = request.data.get('query','').strip()
    query = instructions + "\n\nQuery: " + query1
    response = model.invoke(input=query)

    if isinstance(response, dict) and 'text' in response:
        result = response['text']
    else:
        result = response

    return Response({'message': result})
    