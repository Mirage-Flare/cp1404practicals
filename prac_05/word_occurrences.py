"""
CP1404/CP5632 Practical
Counting the different words in a user string input
"""

word_to_count = {}

user_string = input("Input String: ")
words = user_string.split()
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

words = list(word_to_count.keys())
words.sort()

max_length = len(max(word_to_count, key=len))
for word in words:
    print("{:<{width}} : {}".format(word, word_to_count[word], width = max_length))

