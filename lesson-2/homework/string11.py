string = input("Enter a string: ")
contains_digit = any(char.isdigit() for char in string)
print("Contains digits:", contains_digit)
