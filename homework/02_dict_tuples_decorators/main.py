# Decorators
# task 1
import time

def calcSec(func):
    def inner():
        begin = time.time()
        result = func()
        end = time.time()
        print(f"time: {end - begin} sec")
        return result
    return inner

@calcSec
def getEvenNumbers():
    return list(range(0, 1000, 2)) 

print(getEvenNumbers())


# 2
def replaceChar(func):
    def inner(*args):
        args_ = []
        for i in args:
            if isinstance(i, (int, float)) and i < 0:
                 args_.append(abs(i))
            else: args_.append(i)
        return func(*args_)
    return inner

@replaceChar
def func(*args): return args

print(func(-10, 'blabla', 77, -3, 12))


# Dictionaries
users = {'user1':'123', 'user2':'123qwerty'}

def isValidPass(password):
    if len(password) < 6 or password.isalpha():
        return False
    return True

def addUser(login, password):
    if login in users: print(f"> {login} already exists")
    else:
        if isValidPass(password):
            users[login] = password
            print(f"> {login} added successfully")
        else: print(f"> password isn`t valid")

def removeUser(login):
    if login in users:
        users.pop(login)       
        print(f"{login} deleted")
    else: print(f"{login} not found")

def changePass(login, password):
    if login in users:
        if password != users[login]: 
            users[login] = password
            print('> password have been changed')
        else: print('> this password is already exists')
    else: print('> invalid login')

def checkPasswords():
    for l, p in users.items():
        if isValidPass(p): print(f'{p} ---- password is secure*')
        else: print(f'{p} ---- password isn`t secure*')
            
def getPassByLogin(login):
    if login in users: print(f'> password is: {users.get(login)}')
    else: print(f'> password not found...')

def saveUsers():
    with open("users.txt", "w") as file:
        for key, value in users.items():
            file.write(f"{key} : {value}\n")
        print("> data saved")

def menu():
    while True:
        print("\n\tMenu\n1. Add a new user\n2. Remove a user \n3. Change password \n4. Check passwords \n5. Get password by login \n6. Save users \n0. Exit")
        choice = input('\nChoose an action: ')
        
        if choice.isdigit():
            match int(choice):
                case 1:
                    login = input("\nEnter login: ")
                    password = input("Enter password: ")
                    addUser(login, password) 
                case 2:
                    login = input("\nEnter your login: ")
                    removeUser(login) 
                case 3:
                    login = input("\nEnter your login: ")
                    password = input("Enter your new password: ")
                    changePass(login, password) 
                case 4:
                    print('\n')
                    checkPasswords()
                case 5:
                    login = input("\nEnter your login: ")
                    getPassByLogin(login)
                case 6:
                    saveUsers()
                case 0:
                    print("\nExit...")
                    break
                case _:
                    print('> invalid choice')
        else:
            print("> invalid input ... try again")

menu()
