import json
import os
from datetime import *

def sing_in(users:str, passw:str)->str:
    
    data = {"user": users, "password": passw} # create data to save in dictionary format
    
    if not os.path.exists('conversations'): # Check if the 'conversations' folder exists, if not, create it
        os.makedirs('conversations')
    
    file_path = "conversations/users.json" # Path to the users' file

    if os.path.exists(file_path): # Check if the file exists and load existing users
        with open(file_path, "r", encoding="utf-8") as file:
            existing_data = json.load(file) # Read the existing users data
    else:
        existing_data = [] # If no existing file, initialize an empty list for users
    
    existing_data.append(data) # Append the new user data to the existing list
    
    # Save all users back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4)

def users_conversation():
    data = sing_in(users, passw)
    time = datetime.now().strftime("%I:%M:%S %p")
    currentdate = date.today()
    conversation = {"User":data[users], "date_time": currentdate, "time": time}

if __name__ == "__main__":
    users = str(input("Ingrese el nombre de usuario: "))
    passw = str(input("Ingrese su contraseña: "))
    sing_in(users, passw)