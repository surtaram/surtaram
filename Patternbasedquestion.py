# Pattern-1: Rectangular Star Pattern
n = 6
print("Pattern-1: Rectangular Star Pattern")
for i in range(n):
    for j in range(0, n):
        print("*", end='')
    print()

# Pattern-2: Right-Angled Triangle Pattern


print("Pattern-2: Right-Angled Triangle Pattern")
for i in range(n):
    for j in range(0, i + 1):
        print("*", end='')
    print()
# Pattern - 3: Right-Angled Number Pyramid


print("Pattern - 3: Right-Angled Number Pyramid")
for i in range(n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
# Pattern - 4: Right-Angled Number Pyramid - II


print("Pattern - 4: Right-Angled Number Pyramid - II")
for i in range(n + 1):
    for j in range(1, i + 1):
        print(i, end='')
    print()

# Pattern-5: Inverted Right Pyramid


print("Pattern-5: Inverted Right Pyramid")

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print("*", end="")
    print()

# Pattern - 6: Inverted Numbered Right Pyramid


print('Pattern - 6: Inverted Numbered Right Pyramid')

for i in range(n, 0, -1):
    for j in range(1, i + 1, +1):
        print(j, end='')
    print()

# Pattern - 7: Star Pyramid


print('Pattern - 7: Star Pyramid')

for i in range(n):
    space = ' ' * (n - i - 1)
    star = '*' * (2 * i + 1)
    print(space + star)

# Pattern - 8: Inverted Star Pyramid


print('Pattern - 8: Inverted Star Pyramid')

for i in range(n, 0, -1):
    space = ' ' * (n - i - 1)
    star = '*' * (2 * i - 1)
    print(space + star)

# Pattern - 9: Diamond Star Pattern


print('Pattern - 9: Diamond Star Pattern')

for i in range(n):
    space = ' ' * (n - i - 1)
    star = '*' * (2 * i + 1)
    print(space + star)
for i in range(n, 0, -1):
    space = ' ' * (n - i - 1)
    star = '*' * (2 * i - 1)
    print(space + star)

# Pattern - 10: Half Diamond Star Pattern


print('Pattern - 10: Half Diamond Star Pattern')
# *
# **
# ** *
# ** **
# ** ** *
# ** ** **
# ** ** *
# ** **
# ** *
# **
# *

for i in range(n):
    for j in range(0, i):
        print('*', end='')
    print()

for i in range(n, 0, -1):
    for j in range(0, i, +1):
        print('*', end='')
    print()

# Pattern - 11: Binary Number Triangle Pattern


print("Pattern - 11: Binary Number Triangle Pattern")

for i in range(1, n + 1):
    row = ""
    for j in range(i):
        if (i + j) % 2 == 0:
            row += '1'
        else:
            row += '0'
    print(row)

# Pattern - 12: Number Crown Pattern


print("Pattern - 12: Number Crown Pattern")

# 1    1
# 12  21
# 123321
n = 3
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    space = 2 * (n - i)
    print(' ' * space, end='')

    for j in range(i, 0, -1):
        print(j, end='')
    print()

# Pattern - 13: Increasing Number Triangle Pattern


print("Pattern - 13: Increasing Number Triangle Pattern")

n = 6
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()

# Pattern-14: Increasing Letter Triangle Pattern


print("Pattern-14: Increasing Letter Triangle Pattern")

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=' ')
    print()

# Pattern-15: Reverse Letter Triangle Pattern


print("Pattern-15: Reverse Letter Triangle Pattern")

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=' ')
    print()

# Pattern - 16: Alpha-Ramp Pattern


print("Pattern - 16: Alpha-Ramp Pattern")

for i in range(0, n):
    for j in range(0, i + 1):
        print(chr(65 + i), end=' ')
    print()

# Pattern - 17: Alpha-Hill Pattern

print("Pattern - 17: Alpha-Hill Pattern")

n = 6

for i in range(n):
    print(' ' * (n - i - 1), end='')

    for j in range(i + 1):
        print(chr(65 + j), end='')

    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end='')
    print()
#Pattern-19: Symmetric-Void Pattern


print("Pattern-19: Symmetric-Void Pattern")
for i in range(n):
    print("*" * (n - i), end='')
    print(' ' * (2 * i), end='')
    print("*" * (n - i))

for i in range(n):
    print('*' * (i + 1), end='')
    print(' ' * (2 * (n - i - 1)), end='')
    print('*' * (i + 1))
