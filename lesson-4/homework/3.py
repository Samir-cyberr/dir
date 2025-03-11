def insert_underscore(txt: str) -> str:
    vowels = "aeiouAEIOU"
    result = []
    count = 0
    i = 0
    
    while i < len(txt):
        result.append(txt[i])
        count += 1
        
        if count == 3:
            if i + 1 < len(txt) and (txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] in vowels)):
                result.append(txt[i + 1])
                i += 1
            if i + 1 < len(txt):
                result.append("_")
            count = 0
        
        i += 1
    
    return "".join(result)

# Example usage
txt = input("Enter text: ")
print(insert_underscore(txt))