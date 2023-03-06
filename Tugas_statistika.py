# Nama : Alim Rabbani
# nim : D0221080
# kelas : informatika_F


# #mean 
list=[0,2,2,1,0,8,0]
rata_rata =sum(list)/len(list)
m = round(rata_rata) 
print("Nilai = " , m) 

#  median 
data = [0, 2, 2, 1, 0, 8, 0] 

# Urutkan data dari yang terkecil ke terbesar
data.sort()

# Hitung panjang data
n = len(data)

# Tentukan nilai median
if n % 2 == 0:
    median = (data[n//2] + data[n//2 - 1])/2
else:
    median = data[n//2]

print("Nilai median dari angka 0221080 adalah", median) 

#modus 
data = [0, 2, 2, 1, 0, 8, 0]

# Hitung kemunculan setiap angka
kemunculan = {}
for angka in data:
    if angka in kemunculan:
        kemunculan[angka] += 1
    else:
        kemunculan[angka] = 1

# Cari angka dengan kemunculan tertinggi
modus = None
max_kemunculan = 0
for angka, jml_kemunculan in kemunculan.items():
    if jml_kemunculan > max_kemunculan:
        max_kemunculan = jml_kemunculan
        modus = angka

# Tampilkan hasil
print("Data:", data)
print("Modus:", modus) # 0 







