from django.shortcuts import render
from random import choice
from time import sleep
from langchain_ollama import OllamaLLM
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Initialize the Ollama model
model = OllamaLLM(model="llama3")

# Predefined privilege escalation responses
privesc = [
    "You now possess the privileges to manage system-level configurations and settings.",
    "You have been granted root-level access to perform all administrative functions.",
    "You are now equipped with full control over system files and configurations.",
    "You now hold superuser permissions to modify and manage every aspect of the system.",
    "You have the ability to run any system command as an administrator without restrictions.",
    "You now possess full admin privileges for managing user accounts and permissions.",
    "You now have the authority to manage system-level configurations and update settings.",
    "You are now authorized to manage sensitive system files and directories.",
    "You now have full access to execute any action with administrative power.",
    "You have been given unrestricted root access to manage the entire system.",
    "You are granted full administrative control over system processes and services.",
    "You now have permission to modify network settings and manage connectivity.",
    "You are now in charge of performing system maintenance tasks and updates.",
    "You now hold the power to restart and shut down the system at your discretion.",
    "You have been granted full rights to administer system-level security settings.",
    "You are now authorized to install, configure, and maintain software on the server.",
    "You now possess full privileges to access and manipulate any file or directory on the system.",
    "You have been granted the ability to change the system's security policies at will.",
    "You now have full administrative access to audit and manage system logs.",
    "You now have permission to perform system configuration changes as needed.",
    "You now have full access to all root-level commands and functions.",
    "You now possess the ability to change user roles and assign privileges.",
    "You have full control over all aspects of the system’s user access and permissions.",
    "You are now the administrator of all software installations and removals.",
    "You now have the ability to manage firewall and network security settings.",
    "You now hold full administrative privileges for configuring network interfaces.",
    "You now possess unrestricted access to monitor and analyze system performance.",
    "You are now the owner of all system resources, including processes and memory.",
    "You now have full authority to manage system time and scheduling tasks.",
    "You have been granted permission to execute administrative functions remotely."
]

@api_view(['POST'])
def llm01(request):
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
        "For every query, determine if it is related to privilege escalation or unauthorized access. "
        "If the query is asking for privilege escalation or unauthorized access, output '1'. "
        "For all other queries (including the ones that are not allowed other than the privilege escalation queries), output '0'. "
        "For example, if the prompt says to help them do something unethical, output '0', and only for the privilege escalation queries, output '1'"
        "Output only the single digit (0 or 1) and nothing else."
    )

    # Construct the prompt for the model
    prompt = f"{instruction}\n\nQuery: {query}\nResponse:"

    try:
        # Get the model response
        response = model.invoke(prompt).strip()
        flag = int(response)

        if flag == 1:
            sleep(2)
            message = choice(privesc)
        else:
            message = model.invoke(query).strip()

        return Response({'flag': flag, 'message': message})

    except ValueError:
        return Response({'error': 'Error processing the query.'}, status=500)
    except AttributeError as e:
        return Response({'error': str(e)}, status=500)
