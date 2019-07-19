n1 = raw_input().split()
ans = []
for i in range(len(n1)):
    ans.append(n1[i][::-1])
ansstr = ' '.join(map(str,ans))
print ansstr
