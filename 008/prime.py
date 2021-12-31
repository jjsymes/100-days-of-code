def is_prime(number):
    for n in range(2, number):
        mod = number%n
        if mod == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number.")

print("PRIME NUMBER CHECKER")
number = int(input("Input number you want to check: "))

is_prime(number)
