flowerbed = [1,0,0]
n = 1
def place(flowerbed, n):
    if n == 0:
        return True
    if len(flowerbed) == 1 and flowerbed[0] == 0:
        return True
    elif len(flowerbed) == 1 and flowerbed[0] == 1:
        return False
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        n -= 1
    elif flowerbed[-1] == 0 and flowerbed[-2] == 0:
        flowerbed[-1] = 1
        n -= 1
    for i in range(len(flowerbed) - 3):

        if flowerbed[i] == 1:
            if flowerbed[i+1] == 0 and flowerbed[i+2] == 0 and flowerbed[i+3] == 0:
                flowerbed[i+2] = 1
                n -= 1


    if n <= 0:
        return True
    return False
print(place(flowerbed, n))