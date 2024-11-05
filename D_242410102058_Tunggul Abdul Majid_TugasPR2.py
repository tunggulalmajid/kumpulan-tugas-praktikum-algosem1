"""
Nama  : Tunggul Abdul Majid
NIM   : 242410102058
Kelas : D

"""
print ("="*50)
print ("\tTugas Praktikum pertemuan ke 3")
print ("="*50)

# soal 1 
print ("\nini adalah jawaban no 1 :")
a = [] #list kosong yang akan di isi angka ganjil dan genap
b = [13,3,5,1,7,11,15,9] #list angka ganjil
c = [4,2,6,8,12,14,10] #list angka genap

b.extend (c) #menggabungkan list c kedalam b
a.extend (b) # menggabungkan list b kedalam a 
a.sort() # mengurutkan list a dari angka terkecil ke terbesar

print (f"output nya adalah  : {a[0:16:3]}\n") # menjadikan output nya memiliki selisih 3

#soal 2 
print ("ini adalah jawaban no 2 :")
buah = ["apel", "strawberry", "buah naga", "alpukat", "anggur", "pisang"]
buah = [buah[5] +" "+ buah[0], buah[4] +" "+ buah[1], buah [3] + " " + buah [2]] 
#menggabungkan beberapa value dalam list buah, sehingga membentuk suatu value baru
print (f"sebelum di balik : {buah}")# cek hasil sebelum proses pembalikan
balik = [a[::-1] for a in buah] 
# pembalikan dengan perumpamaan bahwa 'a' adalah huruf yang ada didalam variabel buah
print (f"output : {balik}\n") #output

#soal 3
print ("ini adalah jawaban no 3")
buah = ["pisang","apel","jambu"] #list jenis buah yang dijual
harga = [10000,15000,20000] #list harga dari setiap jenis buah
terjual = [10,5,7] #jumlah terjual tiap jenis buah

untungbuah = [10000*10,15000*5,20000*7] 
#keuntungan penjualan dari setiap jenis buah
total = untungbuah[0] + untungbuah[1] + untungbuah[2]
#total keuntungan penjualan dari seluruh jenis buah
print (f"""
list pendapatan setiap buah :
       {buah[0]} : Rp {untungbuah[0]:,}
       {buah[1]} : Rp {untungbuah[1]:,}
       {buah[2]} : Rp {untungbuah[2]:,}
total keuntungan : Rp {total:,}

""") #list pendapatan tiap jenis buah dan total keuntungan
print ("terima kasih")






