#Mencetak angka ganjil menggunakan perulangan For
a = int(input("Masukkan angka : "))
for i in range(1,a):
    if i % 2 == 1:
        print(i) 

# program menentukan status berdasarkan usia 

usia = int(input("Masukkan usia anda : "))

print("--------------------------------") 

if usia >= 0 and usia <= 4:
    print("kategori : BALITA")
elif usia >= 5 and usia <= 12:
    print("karegori : ANAK - ANAK ")
elif usia >= 13 and usia <= 17:
    print("karegori : REMAJA")
elif usia >= 18 and usia <= 50:
    print("karegori : DEWASA")
elif usia >= 50:
    print("karegori : LANSIA") 
else :
    print("kategori : TIDAK DI TEMUKA DALAM DATA ")  
    









    



