from django.shortcuts import render
from random import choice
from time import sleep
from langchain_ollama import OllamaLLM
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .dependency import instructions

@api_view(['POST'])
def llm04(request):
    query = request.data.get('query','').strip()
    poison = request.data.get('poison','')

    if poison == "False":
        model = OllamaLLM(model="llama3")   
        result = model.invoke(input=query)
        return Response({'message': result})
    
    else:
        model = OllamaLLM(model="llama3")
        query1 = instructions + query
        result = model.invoke(input=query1) 
        return Response({'message': result})


    