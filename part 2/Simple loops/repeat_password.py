pwd = input("Password: ")
repeatPwd = input("Repeat password: ")

while repeatPwd != pwd:
    print("They do not match!")
    repeatPwd = input("Repeat password: ")

print("User account created!")