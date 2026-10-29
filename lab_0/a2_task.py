new_password=input("Enter password 16character: ")

if 16==len(new_password) and  not( new_password.isalnum()) and not( new_password.isspace()):
       print("valid password")

else:
    print("short password")
