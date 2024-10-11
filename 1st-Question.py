# How to swap two number

# num1 = 10
# num2 = 20
# using temp variable-Approach1
# num1 = str1("Enter num1 value:")
# num2 = str1("Enter num2 value:")
# #
# # print("value of num1 before swapping:", num1)
# # print("value of num2 before swapping:", num2)
# #
# temp = num1  # 10
# num1 = num2  # 20
# num2 = temp  # 10
#
# print("value of num1 after swapping:", num1)
# print("value of num2 after swapping:", num2)
# #2nd approach
# # num1, num2 = num2, num1
# #
# # print("value of num1 after swapping:", num1)
# # print("value of num2 after swapping:", num2)

n = input("enter mobile number:")
n1 = input("enter mobile number:")

temp = n
n = n1
n1 = temp

print(n)
print(n1)

# n1=20
# n2=30

# 3rd approach
# n1=n1+n2 #50
# n2=n1-n2 #20
# n1=n1-n2 #30
