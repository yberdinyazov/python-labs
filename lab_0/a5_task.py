import random

random_number=random.randint(0,101)
while True:
    number=input("ugadayde cislo:")
    if not(number.isdigit()):
        continue
    number=int(number)
    if random_number<number:
        print("mense")
    elif random_number>number:
        print("bolse")
    elif random_number==number:
        print("ugadal")
        break
