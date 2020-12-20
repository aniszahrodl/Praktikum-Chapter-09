def bintang(n):
    if n<0:
        print('Angka harus berupa bilangan bulat positif')
    else:
        p='*'
        for i in range(n):
             q= p*(1+2*i)
             print(q.center(2*n))
        



bintang(4)
