import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def create_user_payload():
    name = generate_random_string(10)
    last_name = generate_random_string(10)
    email = f"{generate_random_string(10)}@yandex.ru"
    password = generate_random_string(10)
    username = generate_random_string(10)

    payload = {
        "name": name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "username": username
    }
    return payload
