#Buatlah program yang dapat menerima 2 input angka dengan ketentuan sbb : 
# 1 > jika penjumlahan kedua nilai adalah genap, maka tambah angka 1 
# 2 > jika penjumalahan kedua nilai ganji , maka jumlah di tambah 2 

num1 = int(input("Masukkan angka pertama : ")) 
num2 = int(input("Masukkan angka kedua : "))

sum = num1 + num2
if sum  % 2 == 0:
    sum +=  1 
else :
    sum += 2 
print("hasil penjumalahan : " , sum)  


# training (Sum)
num1 = 100 
num2 = 20 

hallow= num1 + num2  / 4 

print("hasil : " , int(hallow) )     


# penjumalhan 

num1 = 2 
num2 = 3 

sum = num1 + num2

print("penjumalahan dari {} dan {} adalah {}" . format(num1 , num2,sum)) 

# memaikai fungsi input 

num1 = int(input("Angka pertama : ")) 
num2 = int(input("Angka kedua : ")) 

al = num1 + num2 

print("hasil penjumlahan dari {} dan {} adalah : {} " . format(num1 , num2 , al)) 






