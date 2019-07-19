def countt_1(no) :
    stc1 = bin(no)[2:]
    ktc = stc1.count('1')
    return ktc
no1 = int(input())
Lo1 = [ int(x) for xc in input().split()]
Los2 = []
for ic in range(0,no1) :
    Los2.append((countt_1(Lo1[ic]),Lo1[ic]))
Lo3 = sorted(Los2, key=lambda xc : (xc[0],xc[1]),reverse=True)
Lo4 = [xc[1] for xc in Lo3 ]
for ic in range(0,len(Lo4)) :
    print(Lo4[ic])
