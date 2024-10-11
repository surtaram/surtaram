str1 = 'listen'
str2 = "silent"
str3 = 'racecar'
str4 = 'Hello'


def check_anagrams(input1, input2):
    new_str1 = sorted(input1)
    new_str2 = sorted(input2)

    if new_str1 == new_str2:
        print("Given strings are anagrams")
    else:
        print("Given strings are not anagrams")
    return new_str1, new_str1


check_anagrams(str1, str2)


def check_palindrome(input3):
    new_str = input3[::-1]
    if new_str == input3:
        print("string is palindrome")
    else:
        print("string is not palindrome")
    return new_str, input3


check_palindrome(str3)


def char_counts(input4):
    char_count = {}
    for char in input4:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


res = char_counts(str4)


# str4 = 'aabcccccaaa' -> input
# output=a2b1c5a3


def substring_search(input5, sub):
    return sub in input5


substring_search(str4, "ell")

s1 = 'EABCCCDGHRA'
s2 = 'AEDFHR'


# ADH
# DH


def remove_duplicate(input5):
    return "".join(sorted(set(input5), key=input5.index))


res = remove_duplicate(s1)
print(res)
s = 'abcdddccgg'


def string_cmpress(s):
    result = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:

            count += 1
        else:
            result += s[i - 1] + str(count)
            print("result", result)
            count = 1

    result += s[-1] + str(count)
    return result


print(string_cmpress(s))

s3 = 'waterbottle'
s4 = "erbottlewat"


def rotation(s3, s4):
    if len(s3) != len(s4):
        return False
    return s3 in s4 + s4


print(rotation(s3, s4))


def word_order_reverse(input):
    new = input.split()
    output = []
    for char in range(len(new) - 1, -1, -1):
        output.append(new[char])
    reverse_word = " ".join(output)
    return reverse_word


s = 'My name is Surta'
print(word_order_reverse(s))


def reverse_word_without_changing_order(input):
    new = input.split()
    new_list = []
    for word in new:
        new_list.append(word[::-1])
    reverse_content = " ".join(new_list)
    return reverse_content


print(reverse_word_without_changing_order(s))


def reverse_every_second_char(input):
    new = input.split()
    new_list = []
    i = 0
    while i < len(new):
        if i % 2 == 0:
            new_list.append(new[i])
        else:
            new_list.append(new[i][::-1])
        i = i + 1
    reversed = " ".join(new_list)
    return reversed


print(reverse_every_second_char(s))


def even_odd_position(input):
    i = 0
    print("Char persent at event index:- ")
    while i < len(input):
        print(input[i])
        i = i + 2

    i = 1
    print("Char persent at odd index:-")
    while i < len(input):
        print(input[i])
        i = i + 2


s1 = "Mahadev"
even_odd_position(s1)

s11 = "RAVI"
S12 = "TEJAKK"
output = "RJAEVJIA"


def merge_charactor(input1, input2):
    merge_string = ""
    if len(input1) == len(input2):
        for i in range(len(input1)):
            merge_string = merge_string + input1[i] + input2[i]
            # merge_string=merge_string+input2[i]
        return merge_string

    else:
        i, j = 0, 0
        while i < len(input1) or j < len(input2):
            if i < len(input1):
                merge_string = merge_string + input1[i]
                i = i + 1

            if j < len(input2):
                merge_string = merge_string + input2[j]
                j = j + 1

        return merge_string


print(merge_charactor(s11, S12))

input1 = "B4A1D3"
Output = "ABD134"


def sort_char_alpha_digit(input):
    alph = []
    digit = []
    for i in input:
        if i.isdigit():
            digit.append(i)
        else:
            alph.append(i)
    outpuss = " ".join(sorted(alph) + sorted(digit))

    return outpuss


print(sort_char_alpha_digit(input1))


def sort_char_followed_digit(input):
    global x
    outputs = ''
    for i in input:
        if i.isalpha():
            x = i
        else:
            outputs = outputs + x * int(i)
    return outputs


input = 'a4b3c2'
print(sort_char_followed_digit(input))


def char_count(input):
    outputs = ''
    previous = input[0]
    c = 1
    i = 1
    while i < len(input):
        if input[i] == previous:
            c = c + 1
        else:
            outputs = outputs + str(c) + previous
            previous = input[i]
            c = 1
        if i == len(input) - 1:
            outputs = outputs + str(c) + previous
        i = i + 1
    return outputs


input = "aaaabbbbccz"
print(char_count(input))


def GCD(n1, n2):
    gcd = 1
    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
            break
    return gcd


print(GCD(15, 30))


# Check if a number is Armstrong Number or not

# An Amrstrong number is a number that is equal to the sum of its own digits each raised
# to the power of the number of digits.

def isarmstrong(n):
    k = len(str(n))
    sum1 = 0
    for i in str(n):
        sum1 = sum1 + int(i) ** k

    return sum1 == n


def main():
    n = 153
    if isarmstrong(n):
        print("Number is armstrong")
    else:
        print("Not armstrong")


if __name__ == "__main__":
    main()


# Given list of integer to check which numbers are armstrong

def armstrong(l1):
    armstrong1 = []
    for i in l1:
        if i == sum([int(j) ** len(str(i)) for j in str(i)]):
            armstrong1.append(i)
    return armstrong1


l1 = [153, 159, 441, 1]
print("These are armstrong number:-",armstrong(l1))
