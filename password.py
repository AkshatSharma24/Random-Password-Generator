# Program to Generate Random Password

import random
import string

print("----------Welcome to the Password Generator----------")

print("\n")
def password():
    length = int(input("Enter the length of the password: "))
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    combine = "".join(random.choice(letters + numbers + symbols) 
        for i in range(length))
    
    return combine
    
print(password())
