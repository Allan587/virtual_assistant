import requests
from history_management import save_conversations
import shutil
from user_management import select

class VirtualAssistant:
    def __init__(self):
        self.URL_PHP = "https://leoviquez.com/IproyectoIntro/" #Connection to chatGPT via URL
        self.conversacion = [
            {"role": "system", "content": "Eres un asistente útil y conversacional."}
        ]
    def chat_with_php(self, message: str) -> str: #function that allows you to chat with chatGPT
        self.message = message
        self.conversacion.append({"role": "user", "content": self.message}) #Receive a message that will be answered by chatGPT
        
        try:
            respuesta = requests.post(self.URL_PHP, json={"messages": self.conversacion}) #Generates a response based on the user's question or interaction.
            respuesta_json = respuesta.json()
            self.mensaje_respuesta = respuesta_json["choices"][0]["message"]["content"]
            
            self.conversacion.append({"role": "assistant", "content": self.mensaje_respuesta}) #Add the reply to the conversation with the user.
            return self.mensaje_respuesta #Return the response
        
        except Exception as e:

            return f"Error al conectar con el servidor: {e}" #Print a an error in case of error
        
def interact_with_chat(users): #function that allow you to talk with chatbot
    terminal_width = shutil.get_terminal_size().columns #Library that allows you to align text to the screen right side
    assistant = VirtualAssistant()

    while True:
        message = input("Tú: ")  
        if message.lower() in ["salir", "exit", "quit"]:
            text=("¡Hasta luego! :ChatGPT")
            print(text.rjust(terminal_width))
            select()
            break 
        
        respuesta = assistant.chat_with_php(message)
        text=(f"{respuesta} :ChatGPT")
        print(text.rjust(terminal_width))
        save_conversations(users, message, respuesta)

if __name__ == "__main__":
    select()
