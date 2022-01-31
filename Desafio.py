import math
a = int(input("digite a: "))
b = int(input("digite b: "))
c = int(input("digite c: "))


maior1 = (a + b + abs(a - b))/2
maior2 = (maior1 + c + abs(maior1 - c))/2

print("%i eh o maior" %maior2)