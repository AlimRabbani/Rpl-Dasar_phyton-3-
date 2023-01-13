# Buatlah program yang dapat mengetahui penghasilan bersih tiap bulan seseorang dengan ketentuan sbb : 
# 1 . Jika penghasilan minimal 3 juta maka dikenakan pajak 5% 
# 2 . jika pengasilan perbulan minimal 5 juta maka dikenakn pajak 10% 
# 3 . jika jenis pajak pekerjaan adalah PNS maka pajak di tambah 5% 
# 4 . selain itu tidak di kenakan pajak 
# 5 . penghasilan dan jenis pekerjaan di input menggunakan fungsi input pada phyton 


penghasilan = int(input("Masukkan penghasilan / bulan : "))
pekerjaan = input("Masukkan pekerjaan anda : ") 

if pekerjaan == "pns":
    if penghasilan >= 3000000:
        pajak1 = 5/100
        pajak2 = 5/500
        gaji_bersih = penghasilan * pajak1 + pajak2 
        print("Total gaji bersih : " , gaji_bersih)
    elif penghasilan >= 5000000:
        pajak = 10/100
        gaji_bersih = penghasilan * pajak 
        print("Total gaji bersih : " , gaji_bersih ) 
    else : 
        pajak = 0 




    



