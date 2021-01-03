
def number(n):
    if n == 0:
        return 
    while n > 1:
        n %= 4
        if n == 0:
            return True

    return False

print(number(4))