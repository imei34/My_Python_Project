import string
import random

print("""
=====PROGRAM SIMPLE PASSWORD GENERATOR=====
             Create by marccel
""")
char = list(string.ascii_letters + string.digits + '~!@#$%^&*()')
def generatePassword():
    while True:
        length = int(input("Enter password length : "))
        random.shuffle(char)
        password = []
        for i in range(length):
            password.append(random.choice(char))
        random.shuffle(password)
        print("".join(password))
        run_again = input("Generate the password again (y/n)? ")
        if run_again.lower() == 'n':
            break
        else:
            continue
   
generatePassword()