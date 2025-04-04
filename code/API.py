import requests
from history_management import save_conversations
import shutil
from user_management import select

class VirtualAssistant:
    """A class to interact with a virtual assistant using PHP as the backend.
    This class manages the conversation history and sends user messages to the PHP server.
    """
    def __init__(self):
        """Initialize the VirtualAssistant with a conversation history and PHP server URL."""
        self.URL_PHP = "https://leoviquez.com/IproyectoIntro/" 
        self.conversacion = [
            {"role": "system", "content": "Eres un asistente útil y conversacional."}
        ]
    def chat_with_php(self, message: str) -> str: #function that allows you to chat with chatGPT
        """Send a message to the PHP server and receive a response.

        Returns:
            str: The response from the PHP server. 
        """
        self.message = message
        self.conversacion.append({"role": "user", "content": self.message}) 

        try:
            respuesta = requests.post(self.URL_PHP, json={"messages": self.conversacion}) 
            respuesta_json = respuesta.json()
            self.mensaje_respuesta = respuesta_json["choices"][0]["message"]["content"]
            
            self.conversacion.append({"role": "assistant", "content": self.mensaje_respuesta})
            return self.mensaje_respuesta 
        
        except Exception as e:
            return f"Error al conectar con el servidor: {e}" 
        
def interact_with_chat(users): 
    """Interact with the chat interface, allowing the user to send messages and receive responses.
    Args:
        users (str): Used to save conversations by their username as an index
    """
    terminal_width = shutil.get_terminal_size().columns 
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