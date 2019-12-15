# Exercise 1: Build a Python program that tests if an integer is prime. Use a FOR loop.
def is_prime(number):
    if number == 1:
        return False

    for i in range(2, number):
        if (number % i) == 0:
            return False

    return True

# Exercise 2: Build a Python program that tests if an integer is prime. Use a WHILE loop.


# The main program.
while True:
    print("Enter the number to be tested (type <CTRL + C> to exit): ")
    input_number = int(input())
    print(str(input_number) + (" is prime." if is_prime(input_number) else " isn't prime"))
