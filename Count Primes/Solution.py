def checkPrime(num):
    if num == 1 or num == 0:
        return False
    if num == 2:
        return True
    for i in range(2, int(num **1/2) + 1):
        if num % i == 0:
            return False
    return True



for i in range(499979):
    if checkPrime(i):
        print(i)