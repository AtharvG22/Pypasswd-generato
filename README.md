# Password Generator

## Overview
This Python script generates a strong, random password based on user input. The user specifies the number of letters, symbols, and numbers they want in the password, and the script creates a random combination of these characters.

## Features
- Allows users to specify the number of letters, symbols, and numbers in the password.
- Randomly selects characters from predefined lists.
- Shuffles the generated password for better security.
- Simple and interactive command-line interface.

## Usage
1. Run the script using Python.
2. Enter the desired number of letters, symbols, and numbers when prompted.
3. The script will generate and display a randomized password.

## Code
```python
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters_pwd = int(input("Enter the number of letters you want in your password: "))
symbols_pwd = int(input("Enter the number of symbols you want in your password: "))
numbers_pwd = int(input("Enter the number of numbers you want in your password: "))

password = []
for _ in range(letters_pwd):
    password.append(random.choice(letters))
for _ in range(symbols_pwd):
    password.append(random.choice(symbols))
for _ in range(numbers_pwd):
    password.append(random.choice(numbers))

random.shuffle(password)

print("Generated Password: " + "".join(password))
```

## Requirements
- Python 3.x

## Improvements
- Convert the script into a function for reusability.
- Provide an option to generate passwords of random length.
- Add an option to exclude ambiguous characters.

## License
This project is open-source and available for modification and distribution.

