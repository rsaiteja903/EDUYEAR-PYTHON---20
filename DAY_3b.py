#SIMPLE CALUCLATOR
import math as m
def add(a,b):
    return a+b
def diff(a,b):
    return a-b
def mul(a,b):
    return a*b
def fdiv(a,b):
    return a//b
def dediv(a,b):
    return(a/b)
def rmd(a,b):
    return a%b
def power(a,b):
    return m.pow(a,b)

a,b=map(int,input().split())

print("""Addition = {}\nSubtraction = {}\nproduct = {}\nFloor division = {}\nDecimal division = {}\nRemainder = {}\nPower = {}""".format(add(a,b),diff(a,b),mul(a,b),fdiv(a,b),dediv(a,b),rmd(a,b),power(a,b)))

