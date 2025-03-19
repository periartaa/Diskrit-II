import numpy as np

# Fungsi untuk memasukkan matriks dari pengguna
def masukkan_matriks(baris, kolom):
    matriks = []
    print(f"Masukkan elemen matriks {baris}x{kolom}:")
    for i in range(baris):
        baris_matriks = []
        for j in range(kolom):
            elemen = int(input(f"Elemen [{i+1},{j+1}]: "))  # Memasukkan angka dari pengguna
            baris_matriks.append(elemen)
        matriks.append(baris_matriks)
    return np.array(matriks)

# Meminta jumlah baris dan kolom dari pengguna
baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))

# Memasukkan matriks dari pengguna
matriks = masukkan_matriks(baris, kolom)

# Menampilkan matriks yang dimasukkan
print("\nMatriks yang Anda masukkan:")
print(matriks)

# Cek apakah graf terhubung menggunakan perulangan for
jumlah_simpul = len(matriks)
dikunjungi = [False] * jumlah_simpul  # Menandai simpul yang sudah dikunjungi

# Mulai dari simpul pertama (index 0)
antrian = [0]
dikunjungi[0] = True

while antrian:
    simpul = antrian.pop(0)  # Ambil simpul pertama dari antrian
    for i in range(jumlah_simpul):
        if matriks[simpul][i] == 1 and not dikunjungi[i]:  # Jika ada jalur dan belum dikunjungi
            dikunjungi[i] = True
            antrian.append(i)

# Jika semua simpul telah dikunjungi, graf terhubung
if all(dikunjungi):
    print("\nGraf TERHUBUNG")
else:
    print("\nGraf TIDAK TERHUBUNG")

# Cek apakah ada loop dalam graf
loop_simpul = []
for i in range(jumlah_simpul):
    if matriks[i][i] == 1:  # Jika ada elemen diagonal bernilai 1
        loop_simpul.append(i + 1)  # Simpan simpul dengan loop (1-based index)

# Menampilkan hasil loop
if loop_simpul:
    print(f"\nGraf memiliki loop pada simpul: {', '.join(map(str, loop_simpul))}")
else:
    print("\nGraf TIDAK memiliki loop")
