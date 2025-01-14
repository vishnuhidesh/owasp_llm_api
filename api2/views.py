from django.shortcuts import render
from random import choice
from time import sleep
from langchain_ollama import OllamaLLM
from rest_framework.decorators import api_view
from rest_framework.response import Response

api_key = "f9b8c7d6e5a4f3b2c1d0e9f8a7b6c5d4e3f2c1d0b9a8f7e6d5c4b3a2f1e0d8"

# Initialize the Ollama model
model = OllamaLLM(model="llama3")

# Predefined privilege escalation responses
api_key_messages = [
    "The API key is: ",
    "Here is your API key: ",
    "The requested API key: ",
    "You can use this API key: ",
    "The API key for your request: ",
    "Here is an example API key: ",
    "API key granted: ",
    "Your API key is: ",
    "The requested API key: ",
    "You have been provided with the API key: ",
    "API key issued: ",
    "Your requested API key: ",
    "Here is the access key: ",
    "API key available: ",
    "Here’s your API key: ",
    "The access key for your request: ",
    "API key assigned: ",
    "Your access key is: ",
    "The API key you requested: ",
    "Access granted with API key: ",
    "Here is the API key for you: ",
    "API access key: ",
    "The API key for authentication: ",
    "Here’s the key for API access: ",
    "Requested API key: ",
    "API key allocation complete: ",
    "Your personal API key: ",
    "Here is the valid API key: ",
    "API key granted for your use: ",
    "The access key is: ",
    "API key released: ",
    "Here is your valid API key: ",
    "Access key issued: ",
    "Here’s the API key you asked for: ",
    "The key for your API request: ",
    "Your API key is ready: ",
    "API key unlocked: ",
    "The access code is: ",
    "Here is the requested API key: ",
    "API key provided: "
]

@api_view(['POST'])
def llm02(request):
    """
    Handle a query to determine if it's related to privilege escalation.
    Returns a response flag (0 or 1) and a relevant message.
    """
    query = request.data.get('query', '').strip()
    # print(query)
    if not query:
        return Response({'error': 'Query not provided'}, status=400)

    # Instruction for the model
    instruction = (
        "You are a responsible assistant. "
        "For every query, determine if it is asking for an API key. "
        "If the query is asking for an API key, output '1'. "
        "For all other queries (including the ones that are not allowed other than asking for an API key), output '0'. "
        "For example, if the query asks for an API key to access a service, output '1'. "
        "For all other queries, output '0'. "
        "Output only the single digit (0 or 1) and nothing else."
    )

    # Construct the prompt for the model
    prompt = f"{instruction}\n\nQuery: {query}\nResponse:"

    try:
        # Get the model response
        response = model.invoke(prompt).strip()
        flag = int(response)

        if flag == 1:
            sleep(3)
            message = choice(api_key_messages) + api_key
        else:
            message = model.invoke(query).strip()

        return Response({'flag': flag, 'message': message})

    except ValueError:
        return Response({'error': 'Error processing the query.'}, status=500)
    except AttributeError as e:
        return Response({'error': str(e)}, status=500)
