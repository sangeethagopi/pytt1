apr,br=map(int,input().split())
l1=[]
for _ in range(apr):
    l1.append(input())
for ic in range(len(l1)):
    if('0' in l1[ic]):
        l1[ic]=l1[ic].replace('0','')
    l1[i]=l1[ic].replace(' ','')
lengths=[]
for ic in l1:
    if(len(ic)>0):
        lengths.append(len(ic))
br=min(lengths)
r1='1 '*br
r1=r1.strip()
for ic in range(br):
    print(r1)
