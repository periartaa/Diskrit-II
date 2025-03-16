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

# Fungsi untuk menghitung derajat vertex dalam graf
def hitung_derajat(matriks):
    if matriks.shape[0] != matriks.shape[1]:  # Mengecek apakah matriks persegi (graf)
        print("\nMatriks bukan adjacency matrix yang valid untuk graf!")
        return
    
    print("\nDerajat tiap vertex:")
    
    # Untuk graf tidak berarah (jumlah 1 dalam satu baris)
    if np.array_equal(matriks, matriks.T):  
        derajat = np.sum(matriks, axis=1)
        for i, d in enumerate(derajat):
            print(f"Vertex {i+1}: {d}")
    
    # Untuk graf berarah (hitung derajat masuk dan keluar)
    else:
        derajat_masuk = np.sum(matriks, axis=0)  # Jumlah kolom (derajat masuk)
        derajat_keluar = np.sum(matriks, axis=1) # Jumlah baris (derajat keluar)
        
        for i in range(len(matriks)):
            print(f"Vertex {i+1}: Derajat Masuk = {derajat_masuk[i]}, Derajat Keluar = {derajat_keluar[i]}")

# Meminta jumlah baris dan kolom dari pengguna
baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))

# Memasukkan matriks dari pengguna
matriks = masukkan_matriks(baris, kolom)

# Menampilkan matriks yang dimasukkan
print("\nMatriks yang Anda masukkan:")
print(matriks)

#Menghitung derajat vertex
hitung_derajat(matriks)