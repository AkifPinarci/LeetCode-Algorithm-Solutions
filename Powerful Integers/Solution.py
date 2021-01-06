class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        arrx = [1]
        arry = [1]
        incx = x
        incy = y
        while x < bound:
            if x == 1:
                break
            arrx.append(x)
            x *= incx
        while y < bound:
            if y == 1:
                break
            arry.append(y)
            y *= incy
        result = set()
        
        for x in arrx:
            for y in arry:
                if x + y <= bound:
                    result.add(x+y)
        return list(result)