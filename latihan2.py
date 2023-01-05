# menghitung total dari pembelian buku 
# buku = "Phyton for Beginners" 
# harga = 49000
# jumlah_beli = 3 

# total_harga = harga * jumlah_beli

# print("anda telah membeli buku '" + buku +"' sebanyak" + str(jumlah_beli) + "buah") 
# print("total harga yang harus di bayar : Rp. " + str(total_harga)) 


# penjualan buku perpustakaan 

daftar_buku = [
    {'judul ' : 'Buku 1' , 'harga' : 10000},
    {'judul ' : 'Buku 2' , 'harga' : 20000},
    {'judul ' : 'Buku 3' , 'harga' : 10000},
]

def tampilkan_daftar_buku():
    for i, buku in enumerate(daftar_buku): 
        print(i+1 , buku['judul'],'\t',buku['harga']) 

def tampilkan_struk(buku_dipilih , jumlah_buku ,total_harga): 
    print("Struk penjualan buku anak")
    print("Jumlah buku : " , buku_dipilih['judul']) 
    print("jumlah : " , jumlah_buku) 
    print("Total harga : " , total_harga) 

print("Daftar buku anak yang tersedia : " )
tampilkan_daftar_buku() 

while True: 
    pilihan = int(input("Masukkan nomor buku yang ingin di beli( 0 untuk keluar ) : "))
    if pilihan == 0:
        break
    elif pilihan > 0 and pilihan <= len(daftar_buku):
        buku_dipilih = daftar_buku[pilihan - 1] 
        jumlah_buku =int(input("Berapa banyak buku yang ingin anda beli : "))
        total_harga = buku_dipilih['harga'] * jumlah_buku 
        tampilkan_struk(buku_dipilih , jumlah_buku , total_harga)
        break 
    else : 
        print("Mohon masukkan nomor yang valid ") 




