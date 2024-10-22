n = int(input("Enter a number: "))
if n < 0:
    print("Factorial of a negative number does not exist! ")
else:
    factorial = 1

    while n >= 1:
        factorial *= n
        n -= 1

    print("Factorial: ", factorial)