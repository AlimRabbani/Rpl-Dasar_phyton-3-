# saldo = 20000
# lanjut_beli = "y" 
# user = {"Username " : "test" , "pasword" : "test12345" }
# logged = "gagal" 

# def beli_pulsa(p):
#     global saldo 
#     if saldo >=int(p):
#         saldo -= int(p)
#         print("Anda berhasil membeli pulsa : Rp." , p) 
#         print("Sisa saldo anda : Rp. " , saldo) 
#     else : 
#         ("Ops pilsa anda tidak cukup ") 

# while logged == "gagal":
#     print("Mau beli pulsa ? login gan ") 
#     username = input("Masukkan username : ") 
#     pasword = input("Masukkan pasword : ") 
#     if username == user['username'] and pasword == user['pasword']:
#         print("Selamat data " + user['username'])
#         logged = "berhasil" 
#     else : 
#         print("Ops username salah") 

# while lanjut_beli == "y" and logged == "berhasil":
#     print("         Beli pulsa gan    ") 
#     print("---------------------------------")
#     print(" 1 . beli pulsa : Rp. 5.000")
#     print(" 2 . beli pulsa : Rp. 10.000")
#     print(" 3 . beli pulsa : Rp. 20.000")
#     print(" 4 . beli pulsa kostum")
#     print(" 5 . keluar aplikasi")
#     a = int(input("Silahkan pilih pulsa yang ingin anda beli : ")) 
#     if a == 1:
#         beli_pulsa(5000)
#     elif a == 2:
#         beli_pulsa(10000)
#     elif a == 3:
#         beli_pulsa(20000)
#     elif a == 4:
#         beli_pulsa(input("Silahkan masukkan nominal pulsa yang ingin anda beli : Rp ."))
#     elif a == 5:
#         lanjut_beli = "n"
#     else :
#         print("Pilihan tidak tersedia : ") 
#         lanjut_beli = input("Mau isi pulsa lagi y/n  kalo mau lanjut tekan n") 

# Hitung gaji berdasarkan golongan 

nama = input("Masukkan nama : ") 
golongan = input("Masukkan golongan : ") 
jam_lembur = int(input("Masukkan jam lembur : "))

if golongan == "A":
    upah = 200000
elif golongan == "B" :
    upah = 120000
elif golongan == "C":
    upah = 400000
elif golongan == "D":
    upah = 500000
else : 
    print("Tidak ada golongan ") 

if jam_lembur >= 48:
    lembur = jam_lembur - 48 
    bonus = 48 * upah + lembur * 200000
else : 
    bonus = jam_lembur * upah 
print("==========================================")
print("nama : " , nama)
print("golongan : " , golongan) 
print("lama lembur(jam) : " , jam_lembur) 
print("gaji berdasarkan golongan : " , upah) 
print("Bonus : " , bonus) 