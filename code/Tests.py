def user_management(users:str, passw:str)->str:
    """Function that receives users and their password

    Args:
        users (str): user name 
        passw (str): user's password

    Returns:
        str: Returns the users name and password
    """
    users_dictionary = {"user": users , "password": passw}
    return(users_dictionary)

users = str(input('Digita tu nombre: '))
passw = str(input('Digite su su contraseña: '))
user_data = user_management(users, passw)
print(f'User {user_data['user']}') # Prints user's name


