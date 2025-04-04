import json
import os
from datetime import *

def save_conversations(users:str, message:str, respuesta:str)->str:
    """Conversation history management

    Args:
        users (str): _username of the user_
        message (str): _user's message_
        respuesta (str): _chatGPT's response_

    Returns:
        str: _Saves the conversation in a json file_
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%I:%M %p")        
    conversation = {
            "user": f"({current_time}) Tú: {message}",
            "chatbot": f"({current_time}) chatGPT: {respuesta}"
            } 
    if not os.path.exists('conversations'):
        os.makedirs('conversations')
        
    json_file_path = f'conversations/{users}_conversation.json'
    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump({"user": users, "date": current_date, "messages": []}, f, indent=4)

    with open(json_file_path, "r", encoding="utf-8") as file:
        existing_data = json.load(file)  

    if "messages" not in existing_data: 
            existing_data["messages"] = []

    existing_data["messages"].append(conversation)

    with open(json_file_path, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4)
        
def read_conversation(users: str) -> str:
    """Read conversation history from a JSON file.

    Args:
        users (str):its used to read a conversation using the username as an index

    Returns:
        str: The conversation history according to the user
    """
    file_path = f'conversations/{users}_conversation.json'

    if not os.path.exists(file_path):
        return "No conversation history found for this user."

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            conversations = data.get("messages", [])

        if not conversations:
            return "No conversation history found for this user."

        return "\n".join(
            f"{message['user']}\n{message['chatbot']}" for message in conversations
        )
    
    except json.JSONDecodeError:
        return "Error reading the conversation history file."