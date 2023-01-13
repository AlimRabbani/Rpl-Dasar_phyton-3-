print("PROGRAM HITUNG GAJI KARYAWAN\nPT MAJU TERUS")
print("-------------------------------------------")
nama = input("Nama Karyawan :")
jab = input("Jabatan Karyawan [Admin/SPV/Manager] :")
pdd = input("Pendidikan [SMA/D3/S1/S2] :")
jamker = int(input("Jumlah Jam Kerja :"))
print("\n-------------------------------------------\n")

gapok = 4000000
if(jab == "Admin") :
    tunjab = 7/100*gapok
elif(jab == "SPV") :
    tunjab = 20/100*gapok
elif(jab == "Manager") :
    tunjab = 40/100*gapok
else :
       tunjab = 0
 

if(pdd == "SMA" or pdd == "sma") :
    tunpdd = 5/100*gapok
elif(pdd == "D3" or pdd == "d3") :
    tunpdd = 15/100*gapok
elif(pdd == "S1" or pdd == "s1") :
    tunpdd = 30/100*gapok
elif(pdd == "S2" or pdd == "s2") :
    tunpdd = 45/100*gapok
else :
    tunpdd = 0

seljamker = jamker-8
if(seljamker > 0):
    upahLembur = seljamker*25000
else :
    upahLembur = 0

totalgaji = gapok + tunjab + tunpdd + upahLembur

print("Karyawan yang bernama", nama)
print("Honor yang diterima")
print("--- Tunjangan Jabatan     Rp ", tunjab)
print("--- Tunjangan Pendidikan  Rp ", tunpdd)
print("--- Honor Lembur          Rp ", upahLembur)
print("--------------------------------")
print("--- Total Gaji", totalgaji)