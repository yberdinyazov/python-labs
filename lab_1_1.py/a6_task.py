number=input("Enter a number date(DD.MM):")

burclar=[(120, "Козерог"), (218, "Водолей"), (320, "Рыбы"), (420, "Овен"), (520, "Телец"), (621, "Близнецы"), (722, "Рак "), (823, "Лев"), (923, "Дева"),
         (1023, "Весы"), (1122, "Скорпион"), (1221, "Стрелец  ")]
number2=int(number[0]+number[1])
number3=int(number[3]+number[4])

result=(number3*100)+number2

for i in burclar:
    if result <= i[0]:
        print(i[1])
        break
    if result > 1221:
        print("Козерог")