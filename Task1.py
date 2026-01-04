def factorial(n):
    result = 1
    # Loop from 1 to n to multiply numbers
    for i in range(1, n + 1):
        result = result * i
    return result


number = int(input("Enter a number: "))


print("Factorial of", number, "is:", factorial(number))