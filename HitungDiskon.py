# Buatlah program untuk menghitung total pembayaran dari pembelian seorang pelanggan toko . Dalam masalah ini ada ketentuan , apabila pembelian pelanggan tersebut sama dengan atau lebih 100.000 , maka pelanggan mendapatkan diskoun 10% , jika tidak pelanggan tersebut hanya mendapatkan discount 5%

total =int(input("masukkan total belanja anda  : Rp .  ")) 
setelah_diskon = total 

if total <= 100000:
    diskon = total * (5/100)
else:
    diskon = total * (10/100) 

setelah_diskon = total - diskon 

print("Diskonnya yaitu : {} " .format(int(diskon)))
print("harga setelah diskon : {} " .format(int(setelah_diskon))) 

# latihan membuat class dan objek 

class Laptop:
    pass 

laptop1= Laptop()  



laptop1.name = "Laptop ASUS Amd Ryzen 5 5500u" 
laptop1.ukuran = "14 INCI" 
laptop1.color = "Gray color" 

print("========CLASS DAN OBJEK========")
print(laptop1.name) 
print(laptop1.ukuran) 
print(laptop1.color) 







    


