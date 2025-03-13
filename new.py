import numpy as np

# CODE INPUT MATRIKS "Matriks Ketetanggaan"
def input_matrix(rows, cols):
    matrix = []
    print(f"Masukkan elemen matriks {rows}x{cols}:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Elemen [{i+1},{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)

# Fungsi DFS untuk mengecek keterhubungan
def dfs(matrix, node, visited):
    visited[node] = True  # Tandai simpul saat ini sebagai telah dikunjungi
    for neighbor, is_connected in enumerate(matrix[node]):  # Iterasi melalui semua tetangga dari simpul saat ini
        if is_connected and not visited[neighbor]:  # Jika ada koneksi dan tetangga belum dikunjungi
            dfs(matrix, neighbor, visited)  # Lakukan DFS pada tetangga tersebut

# FUNGSI UNTUK MENGECEK APAKAH GRAF TERHUBUNG ATAU TIDAK
def is_connected(matrix):
    rows, cols = matrix.shape
    if rows != cols:
        return False  # Jika bukan matriks persegi, bukan adjacency matrix graf

    visited = [False] * rows
    dfs(matrix, 0, visited)  # Mulai dari simpul pertama

    return all(visited)  # Jika semua simpul dikunjungi, maka graf terhubung

# FUNGSI UNTUK MENGECEK APAKAH GRAF BERARAH ATAU TIDAK
def is_undirected(matrix):
    return np.array_equal(matrix, matrix.T)  # Cek apakah matriks simetris


# Tentukan ukuran matriks
rows = int(input("Masukkan jumlah baris: "))
cols = int(input("Masukkan jumlah kolom: "))
# Input matriks dari pengguna
matrix = input_matrix(rows, cols)
print("Matriks yang Anda masukkan:")
print(matrix)


# Cek apakah graf terhubung atau tidak
if is_connected(matrix):
    print("Graf terhubung.")
else:
    print("Graf tidak terhubung.")
    
# Cek apakah graf berarah atau tidak
if is_undirected(matrix):
    print("Graf tidak berarah.")
else:
    print("Graf berarah.")
