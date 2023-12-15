# make our views
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .secret import api_key
from .models import Conversation
# open AI part
"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
genai.configure(api_key=api_key)

# Set up the model
def Response(text):
    model=genai.GenerativeModel('gemini-pro')
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
    ]

    model = genai.GenerativeModel(model_name="gemini-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    chat = model.start_chat(history=[])

    chat.send_message(text)
    return chat.last.text

# Text pretify
# def format_response(text):
#     if("*" in text):
#         text=text.replace("**","<h1>").replace("*","</h1>")+"\n"
#     else:
#         text=text.strip("```")+"\n"
#     return text


# Open AI end

def index(requests):
    messages=[]
    dic={
        "name":"""Decode stage decode the fetch instruction in this format so that the processor can understand. 
Processor understand only binary format"""

    }
    choice=["hi","hy","nice"]
    update_input=None
    if(requests.method=="POST"):
        user_input=requests.POST.get("user_input")
        try:
            if user_input in dic:
                response=dic[user_input]
                messages.append(response)
            else:
                response=Response(user_input)
                # response=format_response(res)
                # response=Response(user_input)
                messages.append(response)

            update_input=user_input
            conversation=Conversation(user_input=user_input,response=response)
            conversation.save()
        except Exception as e:
            messages.append(e)

    context={
        "messages":messages,
        "user_input":update_input
    }
    return render(requests,"index.html",context)