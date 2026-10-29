my_money=int(input("Enter a number: "))

my_change=[100, 50, 10, 5, 2, 1]

   
for para in my_change:
    adet=my_money // para      
    my_money=my_money % para   
    print(f"{para} : {adet}")