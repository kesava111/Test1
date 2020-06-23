p=[20,10,2,5,9,10,20,76,24,25,32,23,43,45,45,43,9,2,76,82,80]
max=p[0]
n=len(p)
for x in range(1,n):
    if p[x]>max:                                #####max element
        max=p[x]
print(max)