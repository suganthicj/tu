x11,y11=map(int,input().split())
l=list(map(int,input().split()))
t=[]
for i in l:
	if i<y11:
		t.append(i)
t.sort()
print(*t)
