import getpass

def login(username, password):
    # Replace this with actual authentication logic
    if username == "admin" and password == "password":
        print("Login successful!")
    else:
        print("Login failed.")

if __name__ == "__main__":
    user = input("Enter username: ")
    passwd = getpass.getpass("Enter password: ")
    login(user, passwd)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
