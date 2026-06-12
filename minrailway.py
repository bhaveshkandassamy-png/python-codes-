n=int(input())
a=list(map(int,input().split()))
d=list(map(int,input().split()))
a.sort()
d.sort()
i=1
j=0
p=1
ans=1
while i<n and j<n:
    if a[i]<=d[j]:
        p+=1
        ans=max(ans,p)
        i+=1
    else:
        p-=1
        j+=1
print(ans)
