def first_and_last_characters(string):
    if len(string) > 0:
        return string[0], string[-1]
    return None, None

# Example usage
user_string = input("Enter a string: ")
first, last = first_and_last_characters(user_string)

if first and last:
    print(f"First character: {first}")
    print(f"Last character: {last}")
else:
    print("The string is empty.")
