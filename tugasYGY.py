kode = input("masukkan kode : ")
barang = input("Masukkan jenis barang /A/B/C : ")
harga = int(input("Harga barang : "))
diskon = 0

if barang == "A":
    diskon_A = 0.1
    harga_Sebelum_diskon = harga * diskon_A 
    Total_harga_setelah_diskon =  harga_Sebelum_diskon - diskon_A 
    print("jenis barang yang di pilih : " , barang) 
    print("harga sebelum diskon       : " , harga_Sebelum_diskon) 
    print("Total harga setelah diskon : " , Total_harga_setelah_diskon) 
elif barang == "B":
    diskon_B = 0.15
    harga_Sebelum_diskon = harga * diskon_B 
    Total_harga_setelah_diskon  =  harga_Sebelum_diskon- diskon_B
    print("jenis barang yang di pilih : " , barang) 
    print("harga sebelum diskon       : " , harga_Sebelum_diskon) 
    print("total harga setelah diskon : " , Total_harga_setelah_diskon) 
elif barang == "C":
    diskon_C = 0.2
    harga_Sebelum_diskon = harga  * diskon_C
    total_harga_setelah_diskon = harga_Sebelum_diskon - diskon_C
    print("jenis barang yang di pilih : " , barang) 
    print("harga sebelum diskon       : " , harga_Sebelum_diskon) 
    print("total harga setelah diskon : " , total_harga_setelah_diskon) 
else :
    print("coba lagi")
    