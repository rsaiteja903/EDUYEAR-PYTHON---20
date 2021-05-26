#AGE CALUCLATOR

from datetime import date
y=int(input())
current=date.today()
if y<= current.year:
    print(current.year-y,"years old")
else:
    print("Invalid year entered")