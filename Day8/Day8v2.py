#Prime number checker
import math
num_test = int(input("Insert a number to test: "))
def prime_check(n):
    a = round(num_test/2) + 1
    is_prime = True
    for i in range(2,a):
        if num_test%i == 0:
            is_prime = False
    if is_prime:
        print("prime numer")
    else:
        print("not a prime number")

prime_check(n=num_test)

