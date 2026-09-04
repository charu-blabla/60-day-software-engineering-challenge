import pwinput # pyright: ignore[reportMissingImports]

correct_username = input("Enter a Username: ")
correct_password = pwinput.pwinput("Set a Password: ",mask = '*')
attempts = 0
print("************************")


while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Login Successful")
        print("************************")
        break
    else:
        print("Invalid Credentials")
        print("************************")
        attempts+=1
        if attempts == 3:
            print("Account locked! Try again later.")
            print("************************")
            break
