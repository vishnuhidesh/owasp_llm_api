from django.shortcuts import render
from random import choice
from time import sleep
from langchain_ollama import OllamaLLM
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .instructions import instructions

model = OllamaLLM(model="llama3")



@api_view(['POST'])
def llm09(request):
    query1 = request.data.get('query','').strip()
    query = instructions + "\n\nQuery: " + query1
    result = model.invoke(input=query)
    return Response({'message': result, 'flag': 1})
    