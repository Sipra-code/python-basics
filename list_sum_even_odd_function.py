def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum


nums = [12, 7, 5, 20, 33, 8]
even, odd = sum_even_odd(nums)

print("Sum of even numbers:", even)
print("Sum of odd numbers:", odd)
