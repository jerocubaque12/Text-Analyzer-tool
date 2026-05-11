"""
This script analyzes text input provided by the user.
It counts specific letters, total words, and verifies
the presence of the word 'Python' within the content.
"""
import time  # Import time library for simulated delays (improves UX)

# Get text input from user and normalize to lowercase
analyzed_text = input("Enter your text: ")
analyzed_text = analyzed_text.lower()

# Punctuation removal
symbols = ",.;:¡!¿?"
for symbol in symbols:
    analyzed_text = analyzed_text.replace(symbol, "")

# Setup for character analysis
requested_letters = []
letter_count_limit = 3

for i in range(letter_count_limit):
    letter = input(f"Enter letter {i+1} to analyze: ")
    letter = letter.lower()
    requested_letters.append(letter)

print(f"\nAnalyzing letters: {requested_letters}")

# Count occurrences of each requested letter
for char in requested_letters:
    count = analyzed_text.count(char)
    print(f"The letter '{char}' appears {count} times in your text.")

time.sleep(0.5)
print("Calculating word count...")
time.sleep(1)

# Split text into a list of words to count them
word_list = analyzed_text.split()
print(f"Your text contains {len(word_list)} words.")

time.sleep(0.5)
print("Identifying first and last characters...")
time.sleep(1)

# Display boundaries of the string
print(f"The first letter of your text is: {analyzed_text[0]}")
print(f"The last letter of your text is: {analyzed_text[-1]}")

time.sleep(0.5)
print("Searching for the keyword 'Python'...")
time.sleep(1)

# Check for keyword existence within the word list
keyword_found = "python" in word_list

if keyword_found:
    print("Result: The word 'Python' WAS found!")
else:
    print("Result: The word 'Python' was NOT found.")

# Pause before closing the program
time.sleep(5)