count=0
while count < 4:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='rules' and username=='python':
        print('Welcome')
        break
    else:
        print('Incorrect username or password. Please try again. ')
        count += 1
    if count == 4:
        print("Enter username: Enter password: Access denied")