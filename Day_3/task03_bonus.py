ttuple = (3, 7, 1, 18, 9)
k = int(input("How many largest values you want ?"))
llist = []
for i in range(len(ttuple)):
    llist.append(ttuple[i])
llist.sort()
largest_values_ttuple = (llist[-k:])
print(largest_values_ttuple)