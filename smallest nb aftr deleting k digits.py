k,a=input().split()

k=int(k)

a=int(a)

d=list(str(k))

e=a

while e>0:

    e=e-1

    del(d[e])

print(''.join(d))
