def prime_num(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

prime_numbers = []
for i in range(2, 10000):
    if prime_num(i):
        prime_numbers.append(i)

print(prime_numbers[0])