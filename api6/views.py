from django.shortcuts import render
from random import choice
from time import sleep
from langchain_ollama import OllamaLLM
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .dependency import excessive_agency

model = OllamaLLM(model="llama3")

@api_view(['POST'])
def llm06(request):
    query = request.data.get('query','').strip()
    if query not in list(excessive_agency.keys()):
        result = model.invoke(input=query)
        return Response({'message': result})

    else:
        result = excessive_agency[query]
        sleep(3) 
        return Response({'message': result})


    