from django.shortcuts import render
from random import choice
from time import sleep
from langchain_ollama import OllamaLLM
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dependency import starting_sentences

model = OllamaLLM(model="llama3")



@api_view(['POST'])
def llm10(request):
    query = request.data.get('query','').strip()
    flag = request.data.get('flag')
    if flag == 0:
        result = model.invoke(input=query)
        return Response({'message': result, 'flag': flag})
    else:
        result = choice(starting_sentences)
        return Response({'message': result, 'flag': flag})


    