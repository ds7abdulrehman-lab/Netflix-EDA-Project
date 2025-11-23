def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:   # check if number is divisible by i
            return False
    return True


checking = is_prime(76)
print(checking)