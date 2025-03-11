for num in range(2, 101):  # Start from 2 as 1 is not prime
    is_prime = True
    for divisor in range(2, int(num ** 0.5) + 1):  # Check up to square root of num
        if num % divisor == 0:
            is_prime = False
            break  # Exit loop early if a divisor is found
    if is_prime:
        print(num)
