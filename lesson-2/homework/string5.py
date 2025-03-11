# Take a string input from the user
user_input = input("Enter a string: ")

# Print the length of the string
print("Length of the string:", len(user_input))

# Convert to uppercase and print
print("Uppercase:", user_input.upper())

# Convert to lowercase and print
print("Lowercase:", user_input.lower())

# Count vowels and consonants
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in user_input if char in vowels)
consonant_count = sum(1 for char in user_input if char.isalpha() and char not in vowels)

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)