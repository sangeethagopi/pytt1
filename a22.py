stc,st2=input().split()
cost_diff=abs(len(stc)-len(st2))
for i in range(len(sct)):
    if len(st2)==1 and st2[i] in stc:
        break
    if stc[i] != st2[i]:
        cost_diff+=1 
print(cost_diff)
