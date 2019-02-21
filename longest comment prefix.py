N=int(input())

M=str(input())

F=str(input())

b=[]

for i in range(0,len(M)):

    if(M[i]==F[i]):

        b.append(M[i])

c=''.join(b)

print(c)
