sp1=int(input())
arr1=[]
for ic in range(sp1):
	s=input()
	s=list(map(int,s.split(" ")))
	l=len(s)
	for jc in range(l):
		arr1.append(s[jc])
arr1.sort()
print(*arr1,sep=" ")	
