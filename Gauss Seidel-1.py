import numpy as np

# Mencari nilai x1 dan x2 pada SPLTV
# [2*x1 + x2 = 5]
# [x1 + 3*x2 = 5]

BATAS_ITERASI = 100 #Batas Iterasi
print("Menampilkan Matriks :")
A = np.array([[2., 1.],
              [1., 3],])
b = np.array([5.0, 5.0])

# Mencari nilai x1 dan x2 dengan menggunakan metode Gauss Seidel
for i in range(A.shape[0]):                                     # Misalkan nilai x1 dan x2 diasumsikan ,[0 0]
    row = ["{0:2g}*x{1}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print("[{0}] = [{1:2g}]".format(" + ".join(row), b[i]))

x = np.zeros_like(b)
for it_count in range(1, BATAS_ITERASI):
    x_new = np.zeros_like(x)
    print("Iterasi {0}: {1}".format(it_count, x))               # Menampilkan x1 dan x2 [0 0]
    for i in range(A.shape[0]):                                 # Misalkan nilai x1 dan x2 diasumsikan ,[0 0]
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1 :], x[i + 1 :])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    if np.allclose(x, x_new, rtol = 0.05):                      # Batas Toleransi 0.05
        break
    x = x_new
    error = np.dot(A, x) - b

print("Batas Toleransi 0.05")
print("Hasil(x1, x2) : {0}".format(x)) 
print("Nilai Error : {0}".format(error))