# find factorial of a number
import numpy

user_input = int(input("Enter the number: "))
# # 1st approach
# factorial = []
# if user_input > 1:
#     factorial.append(user_input)
#     for i in range(1, user_input + 1):
#         a = user_input - i
#         if a > 0:
#             factorial.append(a)
#         if a == 0:
#             break

# factorial_product = numpy.prod(factorial)
#
# print(f"factorial of {user_input} is:", factorial_product)

# 2nd approach
factorial = 1
if user_input < 0:
    print("Factorial of negative number does not exit")
elif user_input == 0 or user_input==1:
    print(f"factorial of {user_input} is: 1")
else:
    for i in range(1, user_input + 1):
        factorial = factorial * i
    print(f"Factorial of {user_input} is: {factorial}")
