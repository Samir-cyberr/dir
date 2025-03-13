string = input("Enter a string: ")
symbol = input("Enter a replacement symbol: ")
vowels = "AEIOUaeiou"
result = "".join(symbol if char in vowels else char for char in string)
print("Modified string:", result)
