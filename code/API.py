import requests
import json
from user_management import *

class VirtualAssistant:
    def __init__(self):
        self.URL_PHP = "https://leoviquez.com/IproyectoIntro/"
        self.conversacion = [
            {"role": "system", "content": "Eres un asistente útil y conversacional."}
        ]

    def chat_with_php(self, message: str) -> str:
        self.conversacion.append({"role": "user", "content": message})
        
        try:
            respuesta = requests.post(self.URL_PHP, json={"messages": self.conversacion})
            respuesta_json = respuesta.json()
            mensaje_respuesta = respuesta_json["choices"][0]["message"]["content"]
            
            self.conversacion.append({"role": "assistant", "content": mensaje_respuesta})
            return mensaje_respuesta
        
        except Exception as e:
            return f"Error al conectar con el servidor: {e}"
    
if __name__ == "__main__":
    assistant = VirtualAssistant()

    print("Bienvenido al chat con ChatGPT (vía PHP). Escribe 'salir' para terminar.")
    
    while True:
        message = input("Tú: ")  
        if message.lower() in ["salir", "exit", "quit"]:
            print("ChatGPT: ¡Hasta luego!")
            break 
        
        respuesta = assistant.chat_with_php(message)
        print(f"ChatGPT: {respuesta}")