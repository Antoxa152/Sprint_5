import random
import string

def generate_password():
        length = random.randint(7, 10)
        characters = string.ascii_letters + string.digits
        random_password = ''.join(random.choice(characters) for _ in range(length))
        return random_password

def generate_name():
        length = random.randint(6, 10)
        characters = string.ascii_letters
        random_user_name = ''.join(random.choice(characters) for _ in range(length))
        return random_user_name

def generate_email():
        length = 3
        characters = string.digits
        random_user_email = ''.join(random.choice(characters) for _ in range(length)) + '@ya.ru'
        return random_user_email

def generate_incorrect_password():
        length = 5
        characters = string.ascii_letters + string.digits
        random_incorrect_password = ''.join(random.choice(characters) for _ in range(length))
        return random_incorrect_password