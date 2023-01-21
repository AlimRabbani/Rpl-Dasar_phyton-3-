# Program sederhana untuk peminjaman buku di perpustakaan 

# Daftar buku yang tersedia di perpustakaan
daftar_buku = ['Komik One piece', 'Komik Chainshowman', 'Komik Tokyo revengers', 'Komik Attack On Titan']

# Daftar peminjam buku
peminjam_buku = []

# Fungsi untuk meminjam buku
def pinjam_buku(nama, buku):
  # Jika buku tersedia, tambahkan nama peminjam dan hapus buku dari daftar tersedia
  if buku in daftar_buku:
    peminjam_buku.append(nama)
    daftar_buku.remove(buku)
    print(f'{nama} telah berhasil meminjam {buku}')
  else:
    print(f'Maaf, {buku} tidak tersedia')

# Fungsi untuk mengembalikan buku
def kembalikan_buku(nama, buku):
  # Jika nama terdaftar sebagai peminjam buku, hapus nama dari daftar peminjam dan tambahkan buku ke daftar tersedia
  if nama in peminjam_buku:
    peminjam_buku.remove(nama)
    daftar_buku.append(buku)
    print(f'{nama} telah berhasil mengembalikan {buku}')
  else:
    print(f'Maaf, {nama} tidak terdaftar sebagai peminjam {buku}')

# TES CASES

# Pinjam buku 'Buku A' oleh 'Peminjam 1'
pinjam_buku('Luffy', 'Komik One piece')
# Output: 'Peminjam 1 telah berhasil meminjam Buku A'

# Pinjam buku 'Buku B' oleh 'Peminjam 2'
pinjam_buku('Denji', 'Komik Chainshowman')
# Output: 'Peminjam 2 telah berhasil meminjam Buku B'

# Cobalah meminjam buku yang sudah dipinjam oleh orang lain
pinjam_buku('Mitsuya', 'Komik Tokyo revengers')
# Output: 'Maaf, Buku B tidak tersedia'

# Kembalikan buku 'Buku A' oleh 'Peminjam 1'
kembalikan_buku('Eren ', 'Komik Attack On Titan')
# Output: 'Peminjam 1 telah berhasil mengembalikan Buku A'

# Cobalah mengembalikan buku yang tidak dipinjam oleh peminjam
kembalikan_buku('Sasuke', 'Komik Naroto shipunden')
# Output: 'Maaf, Peminjam 1 tidak terdaftar sebagai peminjam