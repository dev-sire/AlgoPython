print("Fibonacci series with 10 elements: ")
first, last = 0, 1
for _ in range(10):
    print(first)
    first, last = last, first + last
