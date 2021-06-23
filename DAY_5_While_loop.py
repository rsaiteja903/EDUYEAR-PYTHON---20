
l=[]
while(1):
        n=input()
        if n!='q':
            l.append(int(n))
        else:
            break
        print("Press 'q' to exist")

print("Sum of integers is : {}".format(sum(l)))