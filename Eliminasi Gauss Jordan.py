import numpy as md
import sys

# Menentukan jumlah dimensi
n = 2

# Membuat Array
Matriks = md.zeros((n,n+1))
x = md.zeros(n)

#Menentukan nilai Matriks
Matriks=md.array([[2, 1, 5],[1, 3, 5]],float)  

# Melakukan Proses Gauss Jordan
for i in range(n):
    if Matriks[i][i] == 0.0:
        sys.exit('Terdapat nol')
        
    for j in range(n):
        if i != j:
            ratio = Matriks[j][i]/Matriks[i][i]

            for k in range(n+1):
                Matriks[j][k] = round(Matriks[j][k] - ratio * Matriks[i][k],2)

if Matriks[0][0] != 1:
    rasio2 = Matriks[0][0] / 1
    for i in range(3):
        Matriks[0][i]=Matriks[0][i]/rasio2

if Matriks[1][1] != 1:
    rasio2 = Matriks[1][1] / 1
    for i in range(3):
        Matriks[1][i]=Matriks[1][i]/rasio2

# Mendapatkan nilai X1 dan X2
for i in range(n):
    x[i] = Matriks[i][n]/Matriks[i][i]

# Menampilkan solusinya
print('Hasilnya adalah : ','\n Matrix A:')
print(Matriks)
for i in range(n):
    print('Nilai X%d = %0.0F' %(i+1,x[i]), end = '\n')