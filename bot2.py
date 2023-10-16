import json
import openai
import gradio
import os
from dotenv import load_dotenv
# import streamlit

# Ensure API key is securely stored and accessed, not hardcoded in the code
load_dotenv()
openai.api_key = os.environ.get("openai_api_key")

# Load data from JSON file
with open("content.json", "r") as file:
    data = json.load(file)

# Extracting data and converting it to a string to be passed as context to the chat model
project_info = json.dumps(data['project_info'], indent=2)
contact_details = json.dumps(data['contact_details'], indent=2)
communication_history = json.dumps(data['communication_history'], indent=2)
instructions = data['instructions']
greeting_message = data['greeting_message']

context = f"Instructions: {instructions}\n\n Project Info: {project_info}\n\nContact Details: {contact_details}\n\nCommunication History: {communication_history}"

# Pre-defined messages with system role
messages = [
    {"role": "system", "content": "You are a real estate broker bot for the Jain Group. Your knowledge and responses are based on the project data provided."},
    {"role": "assistant", "content": context}  # Pass the extracted context here
]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo",  # Ensure you have access to this model
        model="gpt-4", 
        messages=messages
    )
    print(response)
    ChatGPT_reply = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Jain Group Bot")

demo.launch(share=True)
