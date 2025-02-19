def Selection_Sort(x):
  
    n = len(x)
    for i in range(n):
        small = i
        for j in range(i+1, n):
            if x[j] < x[small]:
                small = j
        x[i], x[small] = x[small], x[i]


def anagrams(word1, word2):
  
    word1 = list(word1.lower().strip())
    word2 = list(word2.lower().strip())
    if len(word1) != len(word2):
        return False
    Selection_Sort(word1)
    Selection_Sort(word2)
    return word1 == word2

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
if anagrams(word1, word2):
    print(word1,"and",word2,"are anagrams")
else:
    print(word1, "and", word2, "aren't anagrams")


def anagrams(list1, list2):
  
    if len(list1) == len(list2):
        for ch in list1:
            if ch not in list2:
                return "not anagrams"
            list2.remove(ch)
        return "anagrams"
    else:
        return "not anagrams"


list1 = ['L', 'I', 'S', 'T', 'E', 'N']
list2 = ['S', 'I', 'L', 'E', 'N', 'T', 'T']

print(anagrams(list1, list2))
