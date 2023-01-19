# program aplikasi perpustakaan part 2 

Buku = {
    "Fiksi" : ["Novel" , "Komik" ,"Cerita Bergambar"],
    "Non Fiksi" :["Buku Sains" , "Buku Sejarah" ,"Buku Biografi"]

}

peminjam = {}

def tambah_peminjam(nama , judul):
    tersedia = False
    for daftar_buku in Buku.items():
        if judul in daftar_buku:
            tersedia = True
            break

        if tersedia:
            if nama in peminjam:
                peminjam[nama].append(judul)
            else :
               peminjam[nama] = [judul]
        print(f"Buku {judul} berhasil di pinjam oleh nama{nama}")
        print(f"Maaf , buku {judul} tidak tersedia") 



tambah_peminjam("andi" , "Novel") 
tambah_peminjam("Budi" ,"Buku Sains")
tambah_peminjam("cindy" , "Komik")
tambah_peminjam("David" ,"Buku Matematika")


print(peminjam)
            

    



