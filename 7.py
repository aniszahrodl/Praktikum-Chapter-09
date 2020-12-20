mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
nim=[]
nama=[]
tgl=[]
tmpt=[]
for i in range(len(mhs)):
    a=mhs[i].split(':')
    b=a[2].split('-')
    nim.append(a[0])
    nama.append(a[1])
    tgl.append(b)
    tmpt.append(a[3])
    
ttl=[]
for i in range(len(tgl)):
    p=('/'.join(tgl[i]))
    ttl.append(p)

print('==============================================================')
print('NIM\tNAMA MAHASISWA\t\tTGL LAHIR\tTEMPAT LAHIR')
print('--------------------------------------------------------------')
for x in range(len(mhs)):
    print((nim[x]).ljust(7),(nama[x]).ljust(23),ttl[x].ljust(15),(tmpt[x]).ljust(10))
print('--------------------------------------------------------------')


