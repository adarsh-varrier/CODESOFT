#Calling random packages for printing random Characters
import random
import string

#Take Input from the User
leng=int(input("Enter the Length of password:"))

#Assaign Different Characters to the character Variable
chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

#Assign Random Characters to the Password Variable
password=""

for i in range(leng):
    password += random.choice(chars)

print("Your random password:-",password)