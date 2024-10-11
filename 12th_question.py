# Question: Write a Python function to count the number of occurrences of each character in a given string.

def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


# Test case
print(count_characters("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

s = 'hello'

char_count = {char: s.count(char) for char in s}
print(char_count)

new_dict = dict(sorted(char_count.items(), key=lambda item: item[0]))

print(new_dict)
