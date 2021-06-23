su=0
l=[]
for i in range(int(input("Enter the limit : "))):
    l.append("2"*(i+1))

for i in l:
    su= su+int(i,10)
print(su)