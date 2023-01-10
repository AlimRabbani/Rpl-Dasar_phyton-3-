#program sederhana untuk menghitung saldo dengan bunga bank 
Tabungan = int(input("Masukkan jumlah tabungan : ")) 
lama = int(input("Masukkan jumlah lama menabung(bulan) : ") ) 

if Tabungan <= 1000000:
    sukuBunga = 0.03
    Saldo_Akhir = (Tabungan * sukuBunga) * lama + Tabungan
    print("Karena tabungan anda di bawah 1.000.000 , bunga yang anda dapatkan sebesar 3%")
    print("Maka setelah menabung selama" + str(lama) + "bulan, saldo anda adalah" + str(Saldo_Akhir))
elif Tabungan >= 1000000: 
    sukuBunga = 0.03
    Saldo_Akhir = (Tabungan * sukuBunga) * lama + Tabungan
    print("Karena tabungan anda di atas 1.000.000 , bunga yang anda dapatkan sebesar 4%")
    print("Maka setelah menabung selama" + str(lama) + "bulan, saldo anda adalah" + str(Saldo_Akhir))


    