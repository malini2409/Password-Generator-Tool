# PASSWOARD GENERATOR
import random
import string

def generate_password(length=12, use_special=True, use_digits=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
length = int(input("Enter password length: "))
password = generate_password(length)
print("Generated Password:", password)
