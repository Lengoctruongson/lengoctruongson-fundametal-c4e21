import getpass
print("Hi therem this is a superuser gateway")
u = input("Username: ")
if u == "c4e":
    p = getpass.getpass("Password: ")
    if p == "codechange":
        print("Welcome c4e")
    else:
        print("Password is incorrect")
else:
    print("You are not superuser")