print ("======================== Input bilangan decimal ===============================")
import decimal
nilaidimasukandecimal = float (input("masukan angka decimal anda : "))
print ((decimal.Decimal (nilaidimasukandecimal)))

print ("======================== Input bilangan Pecahan ===============================")
import fractions
nilaidimasukandecimal = float (input("masukan angka decimal anda : "))
print ((fractions.Fraction (nilaidimasukandecimal)))

print ("======================== Input bilangan Pecahan ganda ===============================")
from fractions import Fraction as yang_saya_masukan
print (yang_saya_masukan (int (input ("masukan angka anda yang ingin di pecahkan : "))) + yang_saya_masukan(int (input ("masukan angka ke dua anda di pecahan : "))))
print (1 / yang_saya_masukan(int (input ("masukan angka ke dua anda di pecahan : "))))
print (yang_saya_masukan(int (input ("masukan angka untuk di jumblahkan true atu false : "))) < 2)
print ("============================== Angka Yang Keluar Dari Pecahan =====================================================")
print ("ini lah angka keluar dari pecahan penjumblahan :" , yang_saya_masukan)

print ("============================== input bilangan math ============================================")
print ("==================================input math.cos(math.pi)=====================================================\n")
import math
print ("==================================== input math.pi yang di jumblahkan ===================================================\n")
angka_yang_ingin_dimasukan = int (input ("masukan angka yang ingin di jumblahkan : "))
print (angka_yang_ingin_dimasukan + math.pi)
print ("============================================================================================================")
sads = int (input ("masukan angka yang ingin di jumblahkan : "))
print (sads * math.cos(math.pi))

print ("============================================================================================")
maskan_math_cos = int (input ("masukan angka yang ingin dijumblahkan : "))
print (maskan_math_cos + (math.exp(6)))

print ("==================================input math.lo10(100)=====================================================\n")
mssl = int (input ("masukan angka yang ingin di jumblahkan : "))
print (mssl * (math.log10(100)))

print ("==================================input math.cos(math.pi)=====================================================\n")
fsdgd = int (input ("masukan angka yang ingin di jumblahkan : "))
print (fsdgd + (math.factorial(5)))


print ("===================================== nama yang di jumblahkan ==============================================")
nama_saya = input ("masukan nama anda yang ingin di jumblahkan :")
nama_kedua = input("masukan nama ke dua anda : ")
print ("inilah hasil perhitungan : ", nama_saya[0])
print ("ini yang saya pilih : ", nama_kedua [0:8])
print ("======================== perhitungan dalam penjumblahan ===========================")
print (len (nama_saya), 'nama yang dihitung pertama')
print (len (nama_kedua), 'nama yang di hitung ke dua')
print ('''"inilah hasil nya"''')
print ("=================== penambahan untuk melanjutkan ===============================")
ini_saya = input ()
saya = input ()
masukan = ini_saya + saya
masukan2 = ini_saya * 5
print ("yang keluarkan : ", masukan)
print ("ini yang dikalikan : ", masukan2)

print ("================================== format ==============================================")
masukan_ini = "{0} , {2} , {1} , {3}" .format ("ini","saya","dan","ya")
print (masukan_ini)

print ("================================ posisi ================================")
print (input ("masukan format integer : {0:b}" .format(12)))
print (input ("masukan format float : {0:e}" .format(353.2434)))
x = 12.43256
print ("nilai x anda = %4.2f" %x)
print ("nilai x anda = %5.2f" %x)
asukan_ini = "| {:<10} | {:^10} | | {:>10} |" .format ("ini".upper(),"saya".upper(),"dan".upper())
print (asukan_ini)