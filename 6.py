#data awal
nilaiMhs = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

#masing-masing item dibuat list
NIM=[]
NAMA=[]
MID=[]
UAS=[]
nilai=[]
status=[]
for i in range(len(nilaiMhs)):
    a=nilaiMhs[i]
    b=a['nim']
    NIM.append(b)
    c=a['nama']
    NAMA.append(c)
    d=a['mid']
    MID.append(d)
    e=a['uas']
    UAS.append(e)

#menghitung nilai akhir dan menambahkannya ke dalam list nilai=[]
for x in range(len(MID)):
    nilaiAkhir=(MID[x]+(2*UAS[x]))/3
    nilai.append(round(nilaiAkhir))

#menentukan status dan menambahkannya ke dalam list status=[]
tdk='TIDAK LULUS'
lls='LULUS'
for y in range(len(nilai)):
    if nilai[y]<60:
        status.append(tdk)
    else:
        status.append(lls)
    
#membuat tabel
nim='NIM'
nama='NAMA'
nmid='N.MID'
nuas='N.UAS'
nakhir='N.AKHIR'
stts='STATUS'

print('===========================================================')
print(nim.ljust(8), nama.ljust(8), nmid.rjust(8), nuas.rjust(8), nakhir.rjust(10), stts.rjust(10))
print('-----------------------------------------------------------')
for i in range(len(nilaiMhs)):
    print((NIM[i]).ljust(8), (NAMA[i]).ljust(8), (str(MID[i])).rjust(8), (str(UAS[i])).rjust(8), (str(nilai[i])).rjust(10), (status[i]).rjust(10))
print('-----------------------------------------------------------')



