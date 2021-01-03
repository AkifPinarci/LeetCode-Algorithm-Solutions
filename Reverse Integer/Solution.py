def reverse(x):
    def reverse(num):
        if num < 0:
            num = str(num)[1::]
            num = int(str(num)[::-1])
            return -num
        else:
            num = int(str(num)[::-1])
        return num
    if (-2) ** 31 <= x <= (2 ** 31) - 1:
        return reverse(x)
    else:
        return 0

print (reverse(123123))