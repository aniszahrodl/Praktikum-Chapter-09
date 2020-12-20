def bintang(n):
    if n%2==0:
        print('Angka harus berupa bilangan ganjil')
    else:
        p='*'
        for i in range(n):
             q= p*(1+2*i)
             print(q.center(2*n))
         
        for i in reversed(range(n-1)):
             q= p*(1+2*i)
             print(q.center(2*n))
        



bintang(7)
