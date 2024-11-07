#soal 1 
n = int (input ("masukkan angka >> "))
for i in range (1, n):
    if i % 5 == 0 and i % 3 == 0 :
        print ("FizzBuzz")
        continue
    elif i % 3 == 0 :
        print ("Fizz")
        continue
    elif i % 5 == 0 :
        print ("Buzz")
        continue
    else :
        print (i)

#soal 2 
N = int (input("masukkan angka >> "))
M = int (input("masukkan angka >> "))

tampungan_prima = 0
for i in range (N + 1, M):
    a = 0
    for j in range (1, i+1):
        # print (f" {i} % {j} = {i%j}")
        if i % j == 0 :
            a += 1
        else :
            continue 
    # print (f"ini adalah a : {a}")
    if a == 2 :
        tampungan_prima += 1 
    else :
        continue

print (tampungan_prima)

# print (a)


#soal 3
ini_kata = input ("anu >> ")
ini_kata = ini_kata.lower()
tampungan = []
for i in ini_kata :
    penghitung_huruf = ini_kata.count(i)
    if i in tampungan or i == " " :
        continue
    else : 
        print (f"Huruf: {i} : Jumlah: {penghitung_huruf} ")
    tampungan.append (i)

#soal 4
sebuah = input ("masukkan sebuah kata >> ")
sebuah = sebuah.lower()
ini_e = sebuah.count ("e")
ini_d = sebuah.count("d")
total = ini_d + ini_e
print (total)

#soal 5
anuan_angka = input ("masukkan angka yang anu >> ")
target_angka = input ("masukkan target angka >>")
target_angka = int (target_angka)
# print (type(target_angka))

tampungan_awal = []
tampungan_hasil = []
for i in anuan_angka.split(",") :
    berubah = int (i)
    tampungan_awal.append(berubah)

for i in range (len(tampungan_awal)):
    for j in range (i,len(tampungan_awal)):
        if tampungan_awal[i] + tampungan_awal[j] == target_angka:
            tampungan_hasil.append([tampungan_awal[i],tampungan_awal[j]])
        else :
            continue
print (tampungan_hasil)

#soal 6 
ketik_ini = input ("masukkan kata >> ")

kiri = ["q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"]
kanan = ["y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"]

gimana = True 
for i in range (len(ketik_ini)-1):
    for j in range (len(kiri)):
        if ketik_ini[i] in kiri and ketik_ini[i+1] in kiri:
            gimana = False
            break
        else :
            continue
    
    for a in range (len(kanan)) :
        # print (ketik_ini[i], "=", kanan[a],"|", ketik_ini[i+1], "=", kanan[a])
        if ketik_ini[i] in kanan and ketik_ini[i+1] in kanan :
            gimana = False
            break
        else :
            continue
print (gimana)   

#soal 7 
kata_rusak = "YRnzuijf%mX%tFfoqf"
kata1 = []
kata2 = []
hasil_kata_1 = []
hasil_kata_2 = []
for i in range (len(kata_rusak)):
    if i % 2 == 0 :
        kata1.append(kata_rusak[i])
    else :
        kata2.append(kata_rusak[i])

# print (kata1)
# print (kata2)

for i in range (len(kata1)):
    huruf = ord(kata1[i]) - 5
    done = chr(huruf)
    hasil_kata_1.append(done)
    
    huruf = ord(kata2[i]) - 5
    done = chr(huruf)
    hasil_kata_2.append(done)

for i in hasil_kata_1 :
    print (i, end ="")
print ("")    
for i in hasil_kata_2:
    print (i,end = "")