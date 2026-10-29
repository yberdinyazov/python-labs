while True:
    name_surname=input("Soyisim, isim, babaisim example 'Tom Sam West' : ")

    if name_surname.isdigit():
        print("Hata yapdiniz ")
        continue

   

    my_list= name_surname.split()
    print(f"{my_list[0].capitalize()} {my_list[1][0].capitalize()}.{my_list[2][0].capitalize()}.")
