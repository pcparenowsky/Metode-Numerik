import math

def func(x): 
	return x**2-27 

def bisection(a,b,galaterror,maxIterate):
	if (func(a) * func(b) >= 0):
		print("Tidak ada akar, asumsikan ulang nilai batas a dan b\n") 
		return

	iterasi=0

	while ((b-a) >= galaterror and iterasi < maxIterate):
		iterasi+=1
		
		c = (a+b)/2

		if((func(c)>0 and func(a)<0) or (func(c)<0 and func(a)>0)):
			ket= "Berlawanan tanda"
		else:
			ket=""

		print(iterasi," ",a," ",b," ",c," ",func(a)," ",func(c),ket)
		
		if (func(c) == 0.0): #memeriksa jika fungsi(c) sama dengan 0, maka iterasi dihentikan
			break 		
		#Menentukan sisi mana untuk perulangan
		if (func(c)*func(a) < 0): 
			b = c
		else: 
			a = c 

	print("Nilai Akar dari persamaan tersebut : ","%.5f"%c) #Memberitahu Nilai Akar
	print("Iterasi ke: ","%d"%iterasi) #Memberitahu Perulangan ke berapa

a=int(input("masukan nilai a: ")) #Untuk input Nilai Batas A 
b=int(input("masukan nilai b: ")) #Untuk input Nilai Batas B

errorcode=float(input("Masukan Nilai Galat (Error): ")) #Keterangan Input Nilai A, Nilai B, Nilai Galat
batasiterasi=int(input("Masukan batas Iterasi: ")) #Keterangan Input batas Iterasi
bisection(a, b,errorcode,batasiterasi) 
