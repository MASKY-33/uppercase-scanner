given_sentence = input("Give any sentence: ")

big_letters = []

for char in given_sentence:
    if char.isupper():
        big_letters.append(char)

print(f"Big letters: {', '.join(big_letters)}")
