def login(username, password):
    if username == "python" and password == "rules":
        return True
    else:
        return False

username = input("Enter Username: ")
password = input("Enter Password: ")

if login(username, password):
    print("Welcome")
else:
    print("Access denied")

