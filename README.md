# 🔐 Password Generator Tool

A command-line application to generate strong, customizable passwords. Users can define password length, include digits, and add special characters to enhance security.

---

## ✨ Features
- Generate secure, random passwords
- Choose password length
- Optional inclusion of digits and special characters
- Suitable for beginners practicing loops, functions, and string operations

---

## ✅ Prerequisites
- Python 3.x installed

---

## ▶️ How to Run
1. Save the code as `password_generator.py`
2. Open terminal and run:
```bash
python password_generator.py

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
