import json
import os
from datetime import *
from collections import defaultdict

def keywords(users: str, keywords: list[str]) -> str:
    """Search for multiple keywords in a user's conversation history and group results by keyword.

    Args:
        users (str): Username to identify the conversation file.
        keywords (list[str]): List of keywords to search for.

    Returns:
        str: Messages grouped by the keywords they contain.
    """
    file_path = f'conversations/{users}_conversation.json'

    if not os.path.exists(file_path):
        return "No conversation history found for this user."

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            conversations = data.get("messages", [])

        # Dict to store messages grouped by keyword
        keyword_matches = defaultdict(list)

        for message in conversations:
            user_text = message.get("user", "")
            bot_text = message.get("chatbot", "")
            full_text = f"{user_text} {bot_text}"

            for keyword in keywords:
                if keyword.lower() in full_text.lower():
                    keyword_matches[keyword].append(f"{user_text}\n{bot_text}")
        
        if not keyword_matches:
            return "No messages containing the specified keywords were found."

        # Build the output string grouped by keyword
        output = []
        for keyword in keywords:
            matches = keyword_matches.get(keyword)
            if matches:
                output.append(f"--- Messages with keyword: '{keyword}' ---")
                output.extend(matches)
                output.append("")  # Add spacing

        return "\n".join(output)

    except json.JSONDecodeError:
        return "Error reading the conversation history file."

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
            print("No conversation history found for this user.")

        return "\n".join(
            f"{message['user']}\n{message['chatbot']}" for message in conversations
        )
    
    except json.JSONDecodeError:
        return "Error reading the conversation history file."
    
def summarize_conversations(users: str) -> str:
    """Summary of the user's previous conversations.

    Args:
        users (str): username

    Returns:
        str: summary by date, number of exchanges and examples
    """
    file_path = f'conversations/{users}_conversation.json'
    
    if not os.path.exists(file_path): #It checks if the user has a previous history and if not, it gives a denial message and returns to the chat.
        return "No se encontró historial de conversaciones para este usuario."

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    messages = data.get("messages", [])
    date = data.get("date", "Sin fecha")

    if not messages:
        return "No hay mensajes para resumir."

    resumen = f"\nFecha del archivo: {date}\n"
    resumen += f"Total de intercambios: {len(messages)}\n"

    for i, mensaje in enumerate(messages[:2]):  # Show maximum 2 examples
        user_msg = mensaje["user"].split(") ", 1)[1]
        resumen += f"🔹 Ejemplo {i+1}: {user_msg[:60]}...\n"

    return resumen