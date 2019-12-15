# Exercise 1: Build a Python program that tests if an integer is prime. Use a FOR loop.
def is_prime_using_for(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if (number % i) == 0:
            return False

    return True


# Exercise 2: Build a Python program that tests if an integer is prime. Use a WHILE loop.
def is_prime_using_while(number):
    if number == 1:
        return False

    i = 2
    while i < number:
        if (number % i) == 0:
            return False
        i += 1

    return True


# The main program.
while True:
    print("Enter the number to be tested whether is prime or not (type <CTRL + C> to exit): ")
    input_number = int(input())
    print(str(input_number) + (" is prime" if is_prime_using_for(input_number) else " isn't prime") + ", using a For loop.")
    print(str(input_number) + (" is prime" if is_prime_using_while(input_number) else " isn't prime") + ", using a While loop.\n")
