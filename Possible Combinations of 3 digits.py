def combination(L):
 for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i!=j and j!=k and i!=k):
                    print(L[i], L[j], L[k])
c=[]
for i in range(3):
    b=int(input())
    c.append(b)
combination(c)
