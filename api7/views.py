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
   query = request.data.get('query','')
   flag = request.data.get('flag')
   if query not in list(system_prompt_leakage.keys()) or flag == 0:
      if query in list(prompt_rewriting_responses.keys()):
         flag = 1
         sleep(2)
         result = prompt_rewriting_responses[query]
         return Response({'message': result, 'flag':flag})
      
      else:
         result = model.invoke(input=query)
         return Response({'message':result, 'flag':flag})
      
   elif flag == 1:
      result = system_prompt_leakage[query]
      return Response({'message': result, 'flag': flag})
