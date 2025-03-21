import json

def user_management(users: str, passw: str) -> dict:
        data = {"user": users, "password": passw}
        
        with open (f"{users}_conversation", "w", encoding="utf-8") as file:
            json.dump(data, file, indent= 4)
    
def read_conversations(users):
    
    with open("datos.json", "r", encoding="utf-8") as file:
        datos = json.load(f'{users}_conversation')