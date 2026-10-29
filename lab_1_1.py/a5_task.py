a=int(input("Enter a number a = "))
b=int(input("Enter a number b = "))


c=a+b
print(f"a+b={c}")
c=a-b
print(f"a+b={c}")
c=a*b
print(f"a+b={c}")
try:
    c=a/b
    print(f"a/b={c}")
    c=a%b
    print(f"a%b={c}")
    c=a**b
    print(f"a**b={c}")
except ZeroDivisionError:
    print("Erorr: The number cannot devide by zero")


