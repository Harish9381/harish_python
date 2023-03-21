#3--to remove all tuples from a list where the second element of the tuple is even
l = []
n = int(input("enter num:"))
for x in range(n):
    str = input("enter str:")
    num = int(input("enter num:"))
    l.append((str,num))
print(l)
r = []
for j in l:
    if j[1] % 2 != 0:
        r.append(j)
print(r)
            