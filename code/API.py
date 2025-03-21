import requests
import json

class VirtualAssistant:
    def __init__(self):
        self.URL_PHP = "https://leoviquez.com/IproyectoIntro/"
        self.conversacion = [
            {"role": "system", "content": "Eres un asistente útil y conversacional."}
        ]

    def chat_with_php(self, mensaje: str) -> str:
        self.conversacion.append({"role": "user", "content": mensaje})
        
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
        mensaje = input("Tú: ")  
        if mensaje.lower() in ["salir", "exit", "quit"]:
            print("ChatGPT: ¡Hasta luego!")
            break 
        
        respuesta = assistant.chat_with_php(mensaje)
        print(f"ChatGPT: {respuesta}")

#Constraint: users whith the same name. Solution, check whether the username was created and restict its use.
#Make use of POO to connect frontend to backend and make it readable.
#Research about python encryption libraries.
#Add date time as a reference of the conversation