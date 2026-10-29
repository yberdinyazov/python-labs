#palindrom

new_palindrom=input("enter polindrom:")

newstring=new_palindrom[::-1]
if new_palindrom == newstring:
    print("eto palindrom")

else:
    print("eto ne palindrom")