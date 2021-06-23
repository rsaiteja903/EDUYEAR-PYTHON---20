n=input()

for i in range(len(n)):
    if n[i] in ('a','e','o','i','u') or n[i] in ('A','E','O','I','U'):
        print(i)
    else:
        continue