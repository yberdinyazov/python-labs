
burclar=[(120, "Козерог"), (218, "Водолей"), (320, "Рыбы"), (420, "Овен"), (520, "Телец"), (621, "Близнецы"), (722, "Рак "), (823, "Лев"), (923, "Дева"),
        (1022, "Весы"), (1122, "Скорпион"), (1221, "Стрелец  ")]
found=False
while True:
    birhday=input("Enter a number date(DD.MM):")
    for i in range(4):
        if i==2:
            continue
        if  not(birhday[i].isdigit()): 
            print("Enter a number not a character",end="\n\n")
            continue

    day=int(birhday[0]+birhday[1])
    month=int(birhday[3]+birhday[4])
    
    if  day>31 or month>13:
        print("That date doesn't exist.")
        break
    for i in range(2,12,2):
        if i>5:
            i+=1
        if day==31 and month==i or day==30 and month == 2:
            print("That date doesn't exist.")
            found=True
            break
    if found:
        break
    

    

    result=(month*100)+day

    for i in burclar:
        if result <= i[0]:
            print(i[1])
            break
        if result > 1221:
            print("Козерог")
            break
    print()