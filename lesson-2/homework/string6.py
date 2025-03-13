def contains_substring(main_string, sub_string):
    return sub_string in main_string

# Example usage
main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to check: ")

if contains_substring(main_string, sub_string):
    print("Yes, the main string contains the substring.")
else:
    print("No, the main string does not contain the substring.")