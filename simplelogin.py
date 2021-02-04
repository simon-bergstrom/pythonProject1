userdatabase = {
    "admin" : "password",
    "user" : "password"
}

user_name = input(str("What is your username?"))
user_password = input(str("What is your password"))

def logincheck(username, password):
    for a in userdatabase:
        if a == username:
            if userdatabase[a] == password:
                print("Yaay!")
            else:
                print("Wrong username or password")


logincheck(user_name, user_password)