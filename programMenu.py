def menu():
    print("================Menu Pilihan=============")
    print(" 1 . Masukkan Biodata ") 
    print(" 2 . Input Nilai UTS Dan Nilai UAS") 
    print("==========================================") 

def biodata():
    print("===========================================")
    print("          Masukkan Biodata               ") 
    a = input("Masukkan Nama : ") 
    b = int(input("Masukkan Nim : ")) 
    c = input("Masukkan kelas : ") 
    print("============================================")
    print("============================================")
    print("Nama Anda : " , a ) 
    print("NIM Anda : " , b ) 
    print("Kelas Anda : " , c) 
    print("==============================================")
    print("Menu coba lagi [Y/N] : ") 
    back = input() . upper()
    if back == "Y":
        menu() 
    else : 
        exit()
def nilai():
    print("================================================") 
    a = int(input("Nilai UTS : ")) 
    b = int(input("NIlai UAS : ")) 
    c = (a + b ) / 2 
    print("Nilai akhir anda : " , c , "Semangat") 
    print("=================================================") 
    print("Mau coba lagi [Y/N] : ") 
    back = input() . upper() 
    if back == "Y":
        menu()
    else : 
        exit() 
print("Selamat Datang Di Program Biodata Dan Nilai") 
print("                           by : Alim Rabbani")
print("======================================================") 
menu()

while 1 : 
    pilih = int(input("Masukkan pilihan : ")) 
    if pilih == 1:
        biodata()
    elif pilih == 2:
        nilai()
        print("\n") 

    else : 
        print("Pilihan yang anda masukkan tidak terdaftar ")
        print("Coba lagi [Y/N] : ")
        coba = input() . upper()
        if coba == "Y":
            menu()
        else : 
            exit()  






