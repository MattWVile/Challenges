words = input("Put some words in! ").split()

sorted_unique_words = sorted(set(words), key=str.lower)

print(" ".join(sorted_unique_words))