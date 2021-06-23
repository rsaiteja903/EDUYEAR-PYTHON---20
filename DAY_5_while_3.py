n,i = 0,0
s = input()
res = ""
r=''

while n != (len(s)):
    if n%2==0:
        res = res + (s[n].upper())
    else:
        res=res+s[n]
    n+=1

r="-".join(list(res)).split("- -")
while i<len(r):
    print(r[i])
    i+=1




