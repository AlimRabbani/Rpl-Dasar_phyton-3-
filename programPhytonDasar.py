#1. Jika angka yang diinput habis dibagi 3, maka program akan 
#mencetak pesan “Pride of 3”
#2. Jika angka yang diinput habis dibagi 5, maka program akan 
#mencetak pesan “Pride of 5”
#3. Jika angka yang diinput habis dibagi 3 dan 5, maka program 
#akan mencetak pesan “Master Class”

number = int(input("Input a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("Master Class")
elif number % 3 == 0:
    print("Pride of 3")
elif number % 5 == 0:
    print("Pride of 5")  
    