
l =list(map(int,input()))
s=[]
for i in list(l):
    if i not in s:
        s.append(i)
print(s)