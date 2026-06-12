m=[75,93,65,75,70]
n=len(m)
for i in range(n):
    for j in range(0,n-i-1):
        if m[j]>m[j+1]:
            m[j],m[j+1]=m[j+1],m[j]
print(m)