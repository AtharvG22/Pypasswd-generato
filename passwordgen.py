import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters_pwd=int(input("enter the number of letters you want in your password "))
symbols_pwd=int(input("enter the number of symbols you want in your password "))
numbers_pwd=int(input("enter the number of numbers you want in your password "))


password=[]
for num in range(0,letters_pwd):
    password+=random.choice(letters)
for num in range(0,symbols_pwd):
    password+=random.choice(symbols)
for num in range(0,numbers_pwd):
    password+=random.choice(numbers)


random.shuffle(password)

print(password)





