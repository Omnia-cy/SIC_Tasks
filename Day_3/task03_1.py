short_len = 100
shortest = []
for _ in range(5):
    word = str(input("Enter word: "))
    word_len = len(word)

    if word_len < short_len:
        short_len = word_len
        shortest = [word]

    elif word_len == short_len:
        shortest.append(word)

print(shortest)
