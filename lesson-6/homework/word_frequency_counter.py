import os
import string
from collections import Counter

def get_file_content(filename):
    if not os.path.exists(filename):
        print(f"{filename} not found. Please enter a paragraph to create the file:")
        user_input = input("Enter text: ")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(user_input)
    
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def count_word_frequency(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    word_counts = Counter(words)
    return word_counts

def save_report(word_counts, total_words, output_filename):
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("Word Count Report\n")
        f.write(f"Total Words: {total_words}\n")
        f.write("Top 5 Words:\n")
        for word, count in word_counts.most_common(5):
            f.write(f"{word} - {count}\n")

def main():
    input_filename = "sample.txt"
    output_filename = "word_count_report.txt"
    
    text = get_file_content(input_filename)
    word_counts = count_word_frequency(text)
    total_words = sum(word_counts.values())
    
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in word_counts.most_common(5):
        print(f"{word} - {count} times")
    
    save_report(word_counts, total_words, output_filename)
    print(f"Report saved to {output_filename}")

if __name__ == "__main__":
    main()