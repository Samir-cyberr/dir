# Take a string input from the user
palindrome=input("write any palindrome string:")
#  the reverse of the string
a=palindrome[::-1]
#checking a given string is palindrome
if a==palindrome:
    print(f"{a} is palindrome")
else:
    print(f"{a} is not palindrome")
    