import json
import os
import bcrypt
from datetime import *
  
def user_interface(users):
    Option=int(input("Seleccione la opcion que quiere utilozar\n\n1. Iniciar chat\n2. Ver historial de chats\n3. Palabras clave\n4. Comandos del chat\n(comandos para usar funciones internas del chat)\n5.Salir de la cuenta\n\nOpcion: "))
    if Option==1:
        from API import interact_with_chat as chat
        chat(users)
        user_interface()
    elif Option==2:
        from history_management import read_conversation as read
        print(read(users))
        user_interface()
    elif Option==3:
        from history_management import keywords as key
        key()
        user_interface()
    elif Option==4:
        print("Conandos del chat:\nsalir/exit/quit:[Salir del chat]\nresumir historial/resumen/summary:[muestra un historial de las combersaciones anteriores]")
        user_interface()
    elif Option==5:
        print("Saliendo de la cuenta......")
        select()
    else:
        print("La opcion seleccionada no existe\nPor favor seleccione una de la opciones dadas\n\n")
        user_interface()
    
def history_summary():
    user_data
def login(users: str, passw: str, op:int)->str:
    """User login

    Args:
        users (str): username
        passw (str): user's password
        op (int): selected option

    Returns:
        str: username and password to do a comparison with the one stored in the json file
    """
    file_path = "users/users.json" 

    if not os.path.exists(file_path): 
        print("No hay usuarios registrados.")
        return
    
    with open(file_path, "r", encoding="utf-8") as file: 
        existing_data = json.load(file)

    user_data = next((user for user in existing_data if user["user"] == users), None)

    if user_data is None:
        print("Usuario no encontrado.\nVolviendo al menú principal...")
        select()
        return
    
    stored_hashed_password = user_data["password"]  
    while True:
        if bcrypt.checkpw(passw.encode('utf-8'), stored_hashed_password.encode('utf-8')): 
            print(f'Bienvenido {users}')
            user_interface(users)
            select()
            break
        else:
            print("Contraseña incorrecta.")
            option = input("¿Quieres intentar nuevamente? (s/n): ").strip().lower()
            if option == 's':
                passw = input("Ingrese su contraseña nuevamente: ")
            else:  
                print("Volviendo al menú principal...")
                select()

def sign_up(users:str, passw:str)->str:
    """User registration

    Args:
        users (str): username
        passw (str): user's password

    Returns:
        str: create a new user and saves it in a json file 
    """
    while len(users) < 4:
        print("El nombre del usuario debe tener al menos 4 caracteres.")
        users = input("Ingrese un nombre válido: ")

    while len(passw) < 4:
        print("La contraseña debe tener al menos 4 caracteres.")
        passw = input("Ingrese una contraseña válida: ")

    salt = bcrypt.gensalt()  
    hashed_password = bcrypt.hashpw(passw.encode('utf-8'), salt) 
    data = {"user": users, "password": hashed_password.decode('utf-8')} 

    if not os.path.exists('users'): 
        data = {"user": users, "password": hashed_password.decode('utf-8')} # create data to save in dictionary format

    if not os.path.exists('users'): # Check if the 'users' folder exists, if not, create it
        os.makedirs('users')
    
    file_path = "users/users.json"

    if os.path.exists(file_path): 
        with open(file_path, "r", encoding="utf-8") as file:
            existing_data = json.load(file) 
    else:
        existing_data = []
    
    if any(user["user"] == users for user in existing_data):
        print(f"El usuario '{users}' ya está registrado.\nVolviendo al menú principal...")
        select()
        return
    
    existing_data.append(data) 

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4)
        print(f"Usuario '{users}' registrado con éxito.")

def user_data(): 
    """User data

    Returns:
        str: username and password to compare with the one stored in the json file or create a new one
    """ 
    users = str(input('Ingrese su usuario: ')); passw = str(input('Ingrese su contraseña: ')) 
    return users, passw

def select():
    """Select option
    Returns:
        str: select option to login, sign up or exit
    """
    while True:
        op = int(input("\nBienvenido a tu asistente virtual\n" "1. Inicia sesión con tu usuario\n" "2. Crea un nuevo usuario\n" "3. Salir\n" "Opción: "))
        
        if op == 1:
            users, passw = user_data()
            login(users, passw, op)
            break
        
        if op == 2:
            users, passw = user_data()
            sign_up(users, passw)

        elif op == 3:
            print("Gracias por usar el asistente virtual, tenga un buen dia. ")
            break
        
        else:
            print("La opcion seleccionada no existe o esta mal escrita\n\nSi gusta seleccionar una opsion solo coloque el numero de la opcion\nOpciones: 1 , 2 , 3 ")
    print("El usuario a sido creado con exito.\nVolviendo al menú principal...")
    select()