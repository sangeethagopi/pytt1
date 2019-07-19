ac1=int(input())
b1=0
for i in range(0,a1):
  if(pow(2,i)>ac1):
    break
  b1=ac1-pow(2,i)
print(b1)
