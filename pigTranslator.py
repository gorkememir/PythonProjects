# Take a sentence from user
original = input("Please enter a sentence: ").strip().lower()

# Split it into words
splitted = original.split()

# Define a new list for storing the final sentence
new_words = []

# Start a for loop to scan all the splitted words one by one
for currentWord in splitted:

    # If the first letter of the word in the current loop is a vowel, add "Yay" at the end,
    # and store this as the new_word
    if currentWord[0] in "aieou":
        new_word = currentWord + "Yay"

    # If the first letter is not a vowel, scan through the word until you find a vowel,
    # mark the vowel position, split the word as consonants up to that vowel and the rest.
    # set new_word as such: cons + theRest + "Ay"
    else:
        vowelPos = 0
        for letter in currentWord:
            if letter not in "aieou":
                vowelPos = vowelPos + 1
            else:
                break
        new_word = currentWord[vowelPos:] + currentWord[:vowelPos] + "Ay"

    # Append the new_word to the new_words list
    new_words.append(new_word)

# Turn the list into a sentence, and print it.
output = " ".join(new_words)
print(output)