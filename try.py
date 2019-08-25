def choice():
    print(
        "What do you want? \n 1:Login as admin \n 2:Login as user \n 3:Creat new user \n q:Quit"
    )
    var = input()
    return var


def verify(number):
    if number == 1:
        with open("C:\\Users\\Steve\\Desktop\\scripts\\admin-data.txt", "r") as f:
            lines = f.readlines()
            data1 = lines[1]
            data2 = lines[2]
    if number == 2:
        with open("C:\\Users\\Steve\\Desktop\\scripts\\user-data.txt", "r") as f:
            lines = f.readlines()
            data1 = lines[1]
            data2 = lines[2]
    data1 = data1[:-1]
    data2 = data2[:-1]
    username = input("Enter username:")
    passworld = input("Enter passworld:")
    if username == data1 and passworld == data2:
        return True
    else:
        return False


def loop():
    while True:
        c = choice()
        if c == "1":
            if verify(1):
                print("Logged in succesfully!")
            else:
                print("Incorrect username or passworld")
        elif c == "2":
            if verify(2):
                print("Logged in succesfully!")
            else:
                print("Incorrect username or passworld")
        elif c == "3":
            print("Harom")
        elif c == "q":
            break
        else:
            print("Invalid input")


loop()
