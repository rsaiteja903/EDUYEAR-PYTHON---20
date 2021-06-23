l=list(map(int,input()))
e,o=0,0
for i in l:
    if i %2 ==0:
        e+=1
    else:
        o+=1
print("Total even numbers are :{}\n Total odd numbers are :{} ".format(e,o))
mx,mn=l[0],l[0]
for i in l:
    if mx <i:
        mx=i
    if mn>i:
        mn=i
print("Maximum: {} \nMinimum : {}".format(mx,mn))

s=l[::-1]

if s != l :
    print("Not a palindrome")
else:
    print("Yes list is palindrome")






