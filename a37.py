nnn1=int(input())
li1=list(map(int,input().split()))
a=[1]*nnn1
for ic in range(nnn1):
    if(ic==0):
        if(li1[ic]>li1[ic+1]):
            a[ic]=a[ic]+a[ic+1]
    elif(ic>0):
        if(li1[ic]>li1[ic-1]):
            a[ic]=a[ic]+a[ic-1]
print(sum(a))
