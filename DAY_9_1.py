
def prime_or_not(n):
    c=0
    for i in range(1,n+1):
        if n%i ==0:
            c+=1
        else:
            continue
    if c==2:
        print(f'{n} is prime')
    else:
        print(f'{n} is not prime')
if __name__ =="__main__":
    n= int(input("Enter the number:"))
    prime_or_not(n)
