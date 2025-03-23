import json
import os
from datetime import *

def save_conversations(user_name:str, message:str, respuesta:str)->str : #Funtion that saves user's conversation with chatbot/chatGPT
        current_date = datetime.now().strftime("%Y-%m-%d")    
        current_time = datetime.now().strftime("%I:%M %p")
        
        # create data to save in dictionary format
        conversation = {
            "user": f"({current_time}) Tú: {message}",
            "chatbot": f"({current_time}) chatGPT: {respuesta}"
            } 
    
        if not os.path.exists('conversations'): # Check if the 'conversations' folder exists, if not, create it
            os.makedirs('conversations')
            
        user_folder = f'conversations/{user_name}_conversation' #Check if the 'user' folder exists, if not, create it
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)
        
        json_file_path = f'{user_folder}/{current_date}_conversation.json' # Si el archivo no existe, crearlo con una estructura inicial
        if not os.path.exists(json_file_path):
            with open(json_file_path, 'w', encoding='utf-8') as f:
                json.dump({"user": user_name, "date": current_date, "messages": []}, f, indent=4)

        with open(json_file_path, "r", encoding="utf-8") as file:
            existing_data = json.load(file)  # Cargar datos existentes (debe ser un diccionario)

        if "messages" not in existing_data: # Asegurar que "messages" es una lista dentro del diccionario
            existing_data["messages"] = []

        existing_data["messages"].append(conversation)# Agregar la nueva conversación a la lista "messages"

        with open(json_file_path, "w", encoding="utf-8") as file: # Guardar los datos actualizados en el archivo JSON
            json.dump(existing_data, file, indent=4)
        
def read_conversation(users:str)-> str:
    file_path = (f'conversations/{users}_conversation')
    with open(file_path, 'r', encoding='utf-8'):
        if not os.path.exists(file_path):
            return "No conversation history found for this user."
        
        conversations = []
        for filename in os.listdir(file_path):
            if filename.endswith("_conversation.json"):
                with open(os.path.join(file_path, filename), 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    conversations.extend(data.get("messages", []))

        if not conversations:
            return "No conversation history found for this user."

        return "\n".join(
            f"{message['user']}\n{message['chatbot']}" for message in conversations
        )