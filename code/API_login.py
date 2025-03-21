import json
import os

def user_management():
    # Ask information from the user
    users = str(input("Ingrese el nombre de usuario: "))
    passw = str(input("Ingrese su contraseña: "))
    
    # create data to save in dictionary format
    data = {"user": users, "password": passw}
    
    # Check if the 'conversations' folder exists, if not, create it
    if not os.path.exists('conversations'):
        os.makedirs('conversations')
    
    # Path to the users' file
    file_path = "conversations/users.json"

    # Check if the file exists and load existing users
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            # Read the existing users data
            existing_data = json.load(file)
    else:
        # If no existing file, initialize an empty list for users
        existing_data = []
    
    # Append the new user data to the existing list
    existing_data.append(data)
    
    # Save all users back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4)

user_management()
    
def read_conversations(users):
    
    with open("datos.json", "r", encoding="utf-8") as file:
        datos = json.load(f'{users}_conversation')
