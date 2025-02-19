llist = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
dictionary = {}
for element in llist:
    if element in dictionary:
        dictionary[element] += 1
    else:
        dictionary[element] = 1

print(dictionary)
