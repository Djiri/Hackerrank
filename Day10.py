import sys


n = int(input().strip())
nbin=str()
while n >= 1:
    nbin=str(n%2) + nbin
    n=int(n/2)
#print(nbin)
count=0
tcount=[0]
for i in range(0,len(nbin)):
    if nbin[i] == "1":
        count += 1
    elif nbin[i] == "0":
        tcount.append(count)
        count=0
tcount.append(count)
print(max(tcount))