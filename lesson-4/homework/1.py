from collections import Counter

def uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)
    
    uncommon = []
    
    for num in count1:
        if num not in count2:
            uncommon.extend([num] * count1[num])
    
    for num in count2:
        if num not in count1:
            uncommon.extend([num] * count2[num])
    
    return uncommon

# Example usage
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
print(uncommon_elements(list1, list2))  # Output: [2, 2, 5]