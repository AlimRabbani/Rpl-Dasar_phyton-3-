print("=======================")
print("PROGRAM KALKULUS GAJI")
print("=======================")

print("     | JABATAN |   ")
print("=======================")



print("  |1 . Direktur  |")
print("  |2 . Manager   |")
print("  |3 . karyawan  |")
print("  |4 . OB        |")
print("  |5 . Exit      |") 

pilih = int(input("Masukkan pilihan anda : "))
print("---------------------------") 

if pilih == 1:
    print("")
    print("Kalkulasi gaji direktur")
    gaji = 1000000
    tunjangan =0.25 * gaji 
    PPN =0.1 * gaji
    total =(gaji + tunjangan) - PPN 
    print("==========================================")
    print(" Gaji pokok         : " , gaji) 
    print(" Tunjagan           : " , tunjangan) 
    print(" pajak penghasilan  :" , PPN)
    print('___________________________________________')
    print("Total Gaji DIrektur : " , total) 
    print("============================================")
elif pilih == 2:
    print("")
    print("Kalkulasi gaji Manager")
    gaji = 500000
    tunjangan =0.125 * gaji 
    PPN =0.1 * gaji
    total =(gaji + tunjangan) - PPN 
    print("==========================================")
    print(" Gaji pokok        : " , gaji) 
    print(" Tunjagan          : " , tunjangan) 
    print(" pajak penghasilan :" , PPN)
    print('___________________________________________')
    print("Total Gaji Manager : " , total) 
    print("===========================================")
elif pilih == 3:
    print("")
    print("Kalkulasi gaji Karyawan")
    gaji = 2000000
    tunjangan =0.16 * gaji 
    PPN =0.1 * gaji
    total =(gaji + tunjangan) - PPN 
    print("==========================================")
    print(" Gaji pokok        : " , gaji) 
    print(" Tunjagan          : " , tunjangan) 
    print(" pajak penghasilan :" , PPN)
    print('___________________________________________')
    print("Total Gaji Karyawan: " , total) 
    print("===========================================")
elif pilih == 4: 
    print("")
    print("Kalkulasi gaji OB")
    gaji = 8000000
    tunjangan =0.16 * gaji 
    PPN =0.1 * gaji
    total =(gaji + tunjangan) - PPN 
    print("==========================================")
    print(" Gaji pokok        : " , gaji) 
    print(" Tunjagan          : " , tunjangan) 
    print(" pajak penghasilan :" , PPN)
    print('__________________________________________')
    print("Total Gaji Karyawan: " , total) 
    print("===========================================")
elif pilih == 5: 
    print(" progaram selesai ")
   