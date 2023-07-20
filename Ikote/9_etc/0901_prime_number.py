import math


def is_prime_number_basic(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def is_prime_number_by_square(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':
    x = int(input())
    print(is_prime_number_basic(x))
    print(is_prime_number_by_square(x))
    