import  hashlib

string = "Hello"

cor_username = "admin"
cor_password = "5f4dcc3b5aa765d61d8327deb882cf99"

def login_check(user, password):
    md5_hash = hashlib.md5(password.encode())
    if user == cor_username and md5_hash.hexdigest() == cor_password: # Checks hashed password against password input
        return True
    else:
        return False

while True:
    user_input = input("What is your username?")
    password_input = input("What is your password?")
    if login_check(user_input, password_input) == True:
        print("Yay")
        break
    else:
        print("Try again!")
