def is_prime(n):
    # Start off with the special cases: 1 & 2
    if n == 1:
        # 1 is not a prime
        return False
    elif n == 2:
        # 2 is a prime
        return True
    elif n % 2 == 0:
        # Everything even isn't a prime
        return False
    else:
        # We've checked everything 1, 2 and everything even
        # So loop i through all the odd numbers starting from 3 and check if n is divisible by the i
        # Also note that n / (sqrt(n)*sqrt(n)) = 1 and so stop iterating when i > sqrt(n)
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
    return True
p = int(input().strip())
for a0 in range(p):
    print("Prime" if is_prime(int(input())) else "Not prime")
