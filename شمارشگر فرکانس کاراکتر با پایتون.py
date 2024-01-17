def count_character_frequency(sentence):
    char_frequency = {}
    for char in sentence:
        if char.isalpha():
            char = char.lower()
            char_frequency[char] = char_frequency.get(char, 0) + 1
    return char_frequency

input_sentence = input("Enter a sentence: ")
result = count_character_frequency(input_sentence)

print("Character Frequencies:")
for char, frequency in result.items():
    print(f"{char}: {frequency}")
