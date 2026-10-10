import os

PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))


print("-----LOGIN/REGISTER PAGE-----")

saved_username=None
saved_password=None
existing_usernames=[]
while True:
    print('1.REGISTER')
    print('2.Login')
    print('3.EXIT')

    try:
        user=int(input("ENter the number:"))
    except ValueError:
        print('Enter a valid number:')
        continue

    if user==1:
        print('----Register Page----')
        username=input("Enter the username for registering:")
        if username == '':
             print("Invalid username")
             continue

        if username in existing_usernames:
            print("Username already taken!!! Try a different one")
            continue

        existing_usernames.append(username)
        
        password=input('Enter password to your new account:')
        while username.lower()==password.lower():
            print("Username and Password can't be similar or same")
            password=input("Enter a different password:")

        print("Successfully registered!!")

        with open(os.path.join(PROJECT_FOLDER, "users.txt"), "a") as file:
            file.write(username + "," + password + "\n")

            saved_username = username
            saved_password = password
    elif user==2:
        username_2=input("Enter the username:")
        password_2=input('Enter the password:')

        found=False
        with open(os.path.join(PROJECT_FOLDER, "users.txt"), "r") as file:
            for line in file:
                saved_username, saved_password = line.strip().split(",")

                if saved_username == username_2 and saved_password == password_2:
                    found = True
                    break
        if found:
            print("Login Success!!!")
        else:
            print("Invalid Username or Password")        
    elif user==3:
        print("Thank You For Visting Our Website") 
        break
