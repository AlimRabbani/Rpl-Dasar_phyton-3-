# HITUNG UANG  BERSIH YANG DI TERIMA DARI PENJUALAN TANAH 
Harga_permeter = 300000

luas_tanah = int(input("Luas tanah yang ingin di jual (Meter) = ")) 

total_Harga = Harga_permeter * luas_tanah 

if total_Harga >=50000000:
    pajak = Harga_permeter * 0.03 
    
elif total_Harga >= 100000000:
    pajak = Harga_permeter * 0.05 
else : 
    pajak = Harga_permeter * 0.01 

uang_bersih = total_Harga - pajak 

print("===============================================================================")

print("Total harga jual adalah                                   : Rp . " , total_Harga) 
print("Besarnya pajak yang di berikan adalah                     : Rp. " , pajak) 
print("uang bersih yang di dapatkan dari penjualan tanah sebesar : Rp . " ,uang_bersih)

# Maap kalo salah pak mentor :(

alim = 1

while alim <= 10:
    print('Rungkad:(')
    alim +=1 


# menghitung Luas segitiga 

def Hitung_luas():
    print("<=====start program ===>>>>>")

    alas = float(input("alas = " ))
    tinggi = float(input("tinggi = ")) 
    luas  = ( alas * tinggi) / 2
    print("jadi luas segitiga  sebesar = " , luas)
    print("<<<<<===Progam selesai====>>>>>")
Hitung_luas() 

