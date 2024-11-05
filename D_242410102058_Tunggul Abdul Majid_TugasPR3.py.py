import os # menambahkan library os

def clear (): #fungsi clear 
    os.system("cls") #untuk clear terminal agar terlihat rapi

def enter(): # fungsi enter
    enter = input ("tekan [ENTER] untuk melanjutkan >>") 
    #inputan sebagi pembatas, jika pengguna menekan enter maka program berlanjut

def garis ():# fungsi garis
    print ("="*50) #print = sebanyak 50 kali

def cover(): # fungsi cover
    garis() # memanggil fungsi garis
    print ("oleh oleh algo part 3".center(50)) # print string sebagai cover 
    garis() # memanggil fungsi garis

def ulang(): #fungsi ulang
    garis() #memanggil fungsi garis
    soal = int(input("silahkan pilih soal : [1][2][3] \natau tekan [4] untuk keluar >>"))
    #memberi pilihan kepada user untuk pergi ke soal no 1 sampai 3 atau keluar program
    if soal == 1: #jika input = 1 
        enter () #memanggil fungsi enter
        pertama() #memanggil ke fungsi pertama (sebagai soal pertama)
    elif soal == 2 : #jika inputaan = 2
        enter() #memanggil fungsi enter
        kedua() #memanggil fungsi kedua (sebagai soal ke 2 )
    elif soal == 3 : #jika inputan = 3
        enter () # memanggil fungsi enter
        ketiga() #memanggil fungsi ketiga (sebagai soal ke 3)
    else : # jika inputan bukan 1,2,3 
        print ("terima kasih telah mampir") #print string (keluar program)
    

def awal(): #fungsi awal
    clear() #memanggil fungsi clear
    cover() #memanggil fungsi cover
    
    print("""
Nama  : Tunggul Abdul Majid
NIM   : 242410102058
Kelas : D
""")
    ulang() #memanggil fungsi ulang
    
def pertama(): #fungsi pertama
    clear() # memanggil fungsi clear
    cover() # memanggil fungsi cover
    print ("\njawaban untuk soal 1")
    angka = int (input("silahkan masukkan angka >>")) 
    #memasukkan inputan dari user berupa angka
    if angka < 7 or 14 <= angka <= 17 : #jika inputan berada di kondisi 1 atau 2 maka true
        print (f"utnuk angka {angka} menghasilkan output {True}")
    else : #selain kondisi 1 dan 2 maka false
        print (f"utnuk angka {angka} menghasilkan output {False}")
    ulang() # memanggil fungsi ulang

def kedua ():#fungsi kedua
    clear() # memanggil fungsi clear
    cover () # memanggil fungsi clear
    n = "ahmad" # sebagai nama user asli (acuan)
    rek = 123 # sebagai rekening asli (acuan)
    nama = input ("masukkan nama >>") #inputan user berupa nama
    saldo = 1000000 #saldo dalam rekening
    if nama == n : #jika nama == namma asli
        rekening = int(input ("masukkan no rekening >>"))#inputan no rekening
        if rekening == rek : # jika rekenging = rekening asli
            tarik = int (input("berapa saldo yang ingin anda tarik >>"))
            #inputan jumlah yang ingin ditarik
            enter() # memanggil fungsi enter
            print (f"penarikan berhasil, sisa saldo : Rp {saldo - tarik:,}") 
            # meanmpilkan sisa saldo yang ada di rekening
        else : # jika no rek tidak sesuai
            print ("penarikan gagal, rekening salah")
    else : # jika nama tidak sesuai

        print ("penarikan gagal, nama tidak terdaftar")
    ulang()# memanggil fungsi ulang

def ketiga (): # fungsi ketiga
    clear() # memanggil fungsi clear
    cover() # memanggil fungsi cover
    komponen = ["RAM 16 GB","RTX 9060","Casing"] # list komponen yang akan dibeli
    harga = [800000,12000000,200000] # list harga setiap komponen
    kupon = ["H4L0D3K"] # kode voucher
    hargat = int(harga[0]*95/100 + harga[1]*95/100 + harga[2]*95/100)
    #harga total, harga setiap prodak di diskon 5% kemudian di tambahkan
    print (f"""komponen terbeli :{komponen[0]}
                  {komponen[1]} 
                  {komponen[2]}

total harga : {hargat:,} 
""")
    mau = input ("apakah ada voucher yang ingin digunakan [y]/[t] >>")
    #inputan ingin menggunakan kupon atau tidak
    if mau == "y": # jika ya
        kup = input ("masukkan voucher >>") # inputan kode kupon 
        if kup in kupon : #jika kupon sesuai
            hargat = hargat * 97/100 # total belanja diskon 3% 
            print ("kupon berhasil digunakan")
            enter()

        else : # jika kode kupon tidak sesuai
            print ("kupon anda salah")
            enter()
    else : # jika tidak ingin menggunakan kupon
        enter() # memanggil fungsi enter
    print (f"""komponen terbeli :{komponen[0]}
                  {komponen[1]}
                  {komponen[2]}

total harga : {hargat:,}""") # hasil akhir
    ulang() # memanggil fungsi ulang
    
if __name__=="__main__": #pembatas antara program dan fungsi awal yang akan dipanggil
    awal() # awal dari program