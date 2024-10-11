# check a number is prime or not
# prime :- A prime number is a whole number greater than 1 whose only factors are 1 and itself.
# example:- 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29


def is_prime(n):
    count = 0
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                count = count + 1
                break  # exit the loop if a divisor is found
        if count == 0:
            print("Number is prime")
            return True
        else:
            print("Number is not prime")
    else:
        print("Number is not prime")


is_prime(6)

# prime_number = [num for num in range(1, limit + 1) if is_prime(num)]
#
# print(prime_number)
