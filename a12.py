nc=int(input())
arr=list(map(int,input().split()))
krrc=[]
yeah=0
for i in range(nc):
	if arr[i] in krrc:
		yeah=1
		ans=arr[i]
		break
	else:
		krrc.append(arr[i])
if(yeah==1):
	print(ans)
else:
	print("unique")
