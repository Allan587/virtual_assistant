import json
import os
import bcrypt
from datetime import *

def login(users: str, passw: str):
    file_path = "users/users.json" #Path where users are stored

    #Check if the file exists
    if not os.path.exists(file_path):
        print("No hay usuarios registrados.")
        return
    
    #Load data from the JSON file
    with open(file_path, "r", encoding="utf-8") as file:
        existing_data = json.load(file)

    # Search for the user in the database
    user_data = next((user for user in existing_data if user["user"] == users), None)

    # If the user does not exist, display an error message
    if user_data is None:
        print("Usuario no encontrado.")
        return

    # Compare the entered password with the stored (encrypted) password
    stored_hashed_password = user_data["password"].encode('utf-8')  # We convert to bytes

    #Compare the entered password with the stored one
    if bcrypt.checkpw(passw.encode('utf-8'), stored_hashed_password):
        print(f"Bienvenido, {users}!") #correct password message
    else:
        print("Contraseña incorrecta.")#incorrect password message

def sign_up(users:str, passw:str)->str:

    while len(users) < 4: #A while loop is started that restricts the creation of users with less than 4 characters.
        print("El nombre del usuario debe tener al menos 4 caracteres.")
        users = input("Ingrese un nombre válido: ")

    while len(passw) < 4: #A while loop is started that restricts the creation of users with less than 4 characters.
        print("La contraseña debe tener al menos 4 caracteres.")
        passw = input("Ingrese una contraseña válida: ")

    # Encrypt the password before saving it
    salt = bcrypt.gensalt()  # Generates a random "salt"
    hashed_password = bcrypt.hashpw(passw.encode('utf-8'), salt)  # Encrypt the password

    data = {"user": users, "password": hashed_password.decode('utf-8')} # create data to save in dictionary format
    
    if not os.path.exists('users'): # Check if the 'users' folder exists, if not, create it
        os.makedirs('users')
    
    file_path = "users/users.json" # Path to the users' file

    if os.path.exists(file_path): # Check if the file exists and load existing users
        with open(file_path, "r", encoding="utf-8") as file:
            existing_data = json.load(file) # Read the existing users data
    else:
        existing_data = [] # If no existing file, initialize an empty list for users
    
    if any(user["user"] == users for user in existing_data):
        print(f"El usuario '{users}' ya está registrado.")
        return
    
    existing_data.append(data) # Append the new user data to the existing list
    
    # Save all users back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4)
        print(f"Usuario '{users}' registrado con éxito.")


def select():
    while True:#A while loop is started to execute the selection until an option is chosen.

        #op is the user's choice
        op = int(input("\nBienvenido a tu asistente virtual\n"
                           "1. Inicia sesión con tu usuario\n"
                           "2. Crea un nuevo usuario\n"
                           "3. Salir\n"
                           "Opción: "))
            
        

        if op == 1:#If you selected 1, the "def login" will start
            users = str(input("Ingrese el nombre de usuario: "))
            passw = str(input("Ingrese su contraseña: "))
            login(users, passw)
        
        elif op == 2:#If you selected 2, the "def login" will start
            users = str(input("Ingrese el nombre de usuario: "))
            passw = str(input("Ingrese su contraseña: "))
            sign_up(users, passw)

        elif op == 3:#If you selected 3, the program stops
            print("Gracias por usar el asistente virtual, tenga un buem dia. ")
            break

        else:#If you select another option, an error message appears and you return to your selection.
            print("La opcion seleccionada no existe o esta mal escrita\n\nSi gusta seleccionar una opsion solo coloque el numero de la opcion\nOpciones: 1 , 2 , 3 ")
select()