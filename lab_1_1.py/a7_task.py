konusma_suresi=int(input("Enter the number of minutes used: "))
mesaj_suresi=int(input("Enter the number of SMS messages sent: "))
inter_suresi=int(input("Enter the amount of internet traffic used (in MB): "))

if konusma_suresi<60:
    konusma_suresi-=60*(0.89)