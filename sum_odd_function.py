def sum_odd(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total

num = int(input("Enter a number: "))
print("Sum of odd numbers:", sum_odd(num))
