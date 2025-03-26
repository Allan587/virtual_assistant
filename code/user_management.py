import json
import os
import bcrypt
from datetime import *
  
def login(users: str, passw: str)->str:
    file_path = "users/users.json" #Path where users are stored

    if not os.path.exists(file_path): #Check if the file exists
        print("No hay usuarios registrados.")
        return
    
    with open(file_path, "r", encoding="utf-8") as file: #Load data from the JSON file
        existing_data = json.load(file)

    user_data = next((user for user in existing_data if user["user"] == users), None) # Search for the user in the database

    if user_data is None: # If the user does not exist, display an error message
        print("Usuario no encontrado.\nVolviendo al menú principal...")
        select()
        return

    stored_hashed_password = user_data["password"]  # Compare the entered password with the stored (encrypted) password and convet to byte

    while True:
        if bcrypt.checkpw(passw.encode('utf-8'), stored_hashed_password.encode('utf-8')): #Compare the entered password with the stored one
            print(f'Bienvenido {users}')
            from API import interact_with_chat
            interact_with_chat(users)
            return
        else:
            print("Contraseña incorrecta.")  # Error mensage
            option = input("¿Quieres intentar nuevamente? (s/n): ").strip().lower()

            if option == 's':  # If you choose to continue, it will ask for the password again
                passw = input("Ingrese su contraseña nuevamente: ")
            else:  # If you choose to exit, break the loop and terminate the function
                print("Volviendo al menú principal...")
                select()
                return

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
        print(f"El usuario '{users}' ya está registrado.\nVolviendo al menú principal...")
        select()
        return
    
    existing_data.append(data) # Append the new user data to the existing list

    with open(file_path, "w", encoding="utf-8") as file: # Save all users back to the file
        json.dump(existing_data, file, indent=4)
    print("El usuario a sido creado con exito.\nVolviendo al menú principal...")
    select()

def user_data(): #Take username and password from the users
    users = str(input('Ingrese su usuario: ')); passw = str(input('Ingrese su contraseña: ')) #Contains username and password
    return users, passw

def select(): #Function that allows you to select the process to be performed
    while True:
        op = int(input("\nBienvenido a tu asistente virtual\n" "1. Inicia sesión con tu usuario\n" "2. Crea un nuevo usuario\n" "3. Salir\n" "Opción: "))
        
        if op == 1:#If you selected 1, the "def login" will start
            users, passw = user_data()
            login(users, passw)
            break
        
        if op == 2:#If you sele
            users, passw = user_data()
            sign_up(users, passw)
            break

        if op == 3 :#If you selected 3, the program stops
            print("Gracias por usar el asistente virtual, tenga un buen dia. ")
            break

        else:#If you select another option, an error message appears and you return to your selection.
            print("La opcion seleccionada no existe o esta mal escrita\n\nSi gusta seleccionar una opsion solo coloque el numero de la opcion\nOpciones: 1 , 2 , 3 ")