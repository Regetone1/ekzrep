import random 
a = int(input())
b = int(input())
c = []
d = []
for a in range(a):
    c = [random.randint(0, 100) for i in range(b)]
    d.append(c)
print(d)