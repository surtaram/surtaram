# Question: Write a Python function to remove duplicate characters from a string while preserving the original order.

def remove_duplicates(s):
    seen = set()
    result = ''
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result


# Test case
print(remove_duplicates("hello"))  # Output: 'helo'
