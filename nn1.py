import math
spisok1=[1, 0, 2, -3, 8, 9]
def log(i):
    if i>0:
        return math.log1p(i)
    else:
        return'None'
def my_log(spisok:list):
    return [log(inn) for inn in spisok ]

print(my_log(spisok1))