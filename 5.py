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
    
#membuat tabel
nim='NIM'
nama='NAMA'
nmid='N.MID'
nuas='N.UAS'

print('====================================================')
print(nim.ljust(8), nama.ljust(8), nmid.rjust(8), nuas.rjust(8))
print('----------------------------------------------------')
for i in range(len(nilaiMhs)):
    print((NIM[i]).ljust(8), (NAMA[i]).ljust(8), (str(MID[i])).rjust(8), (str(UAS[i])).rjust(8))
print('----------------------------------------------------')

