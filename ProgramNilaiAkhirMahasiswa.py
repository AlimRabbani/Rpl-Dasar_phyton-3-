print("=======================================")
print ( "NILAI MATA KULIAH BAHASA PEMROGRAMAN ")
print("=======================================") 

nama =input("Masukkan Nama         : ") 
uts = int(input ("Masukkan Nilai UTS    : ")) 
uas = int(input("Masukkan Nilai UAS     : ")) 
tugas = int(input("Masukkan Nilai Tugas : ")) 
print("========================================")  
print ("Nama       :" , nama ) 
print("Nilai UTS   :" , uts) 
print("Nilai UAS   :" , uas) 
print("Nilai Tugas :" , tugas)   
akhir =(uts+uas+tugas) / 3   
print("Nilai Akhir : " , akhir)  
print("===========================================")  

if akhir >= 80 and akhir < 100 :
      print("Predikat : A ") 
      print("Keterangan : Lulus") 
elif akhir >= 70 and akhir < 80 : 
    print("Predikat : B ") 
    print("Keterangan : Lulus") 
elif akhir >= 50 and akhir < 70 : 
    print("Predikat : C ") 
    print("Keterangan : Tidak Lulus") 
elif akhir >= 40 and akhir < 50 : 
    print("Predikat : D ") 
    print("Keterangan : Tidak Lulus / kita ketemu lagi tahun depan")  
elif akhir >= 0 and akhir < 40 : 
    print("Predikat : E ") 
    print("Keterangan : Tidak Lulus / kita ketemu lagi tahun depan")   
print("================================================")










