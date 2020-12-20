import random

def shuffleString(x, n):
    List=[]
    for i in range(n):
        p=list(x)
        random.shuffle(p)
        q= ''.join(p)
        List.append(q)
    print(List)



shuffleString('gurita',3)
