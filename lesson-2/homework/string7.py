def replace_word(sentence, old_word, new_word):
    return sentence.replace(old_word, new_word)

# Example usage
sentence = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

new_sentence = replace_word(sentence, old_word, new_word)
print("Updated sentence:", new_sentence)