
m,n= map (int, input("Enter m,n").split())

for i in range(m,n+1):
    if i%5==0 and i%7==0:
        print(i)
