number=input("Enter a number date:")



number2=int(number[0]+number[1])
number3=int(number[3]+number[4])

if number3==1:
    if number2<19:
        print("Козерог")
    else:
        print("Водолей")

elif number3==2:
    if number2<18:
        print("Водолей")
    else:
        print("Рыбы")

elif number3==3:
    if number2<20:
        print("Рыбы")
    else:
        print("Овен")

elif number3==4:
    if number2<19:
        print("Овен")
    else:
        print("Телец")

elif number3==5:
    if number2<20:
        print("Телец")
    else:
        print("Близнецы")

elif number3==6:
    if number2<20:
        print("Близнецы")
    else:
        print("Рак")

elif number3==7:
    if number2<19:
        print("Рак ")
    else:
        print("Лев")

elif number3==8:
    if number2<19:
        print("Лев")
    else:
        print("Дева")

elif number3==9:
    if number2<19:
        print("Дева")
    else:
        print("Весы")

elif number3==10:
    if number2<19:
        print("Весы")
    else:
        print("Скорпион")

elif number3==11:
    if number2<19:
        print("Скорпион")
    else:
        print("Стрелец")

elif number3==12:
    if number2<19:
        print("Стрелец")
    else:
        print("Козерог")