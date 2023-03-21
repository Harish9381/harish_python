 #2-------iterate over a list of tuples and print out the first element of each tuple----
list_tup = []
n = int(input("enter n:"))
for x in range(n):
    word = input("enter word:")
    num = int(input("enter num:"))
    res = word[0],num
    list_tup.append((res))
print(list_tup)