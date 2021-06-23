

def pattern(n):
    print(n)
    if n<=0:
        return
    pattern(n-5)
    print(n)




n=int(input("Enter the number : "))
pattern(n)
