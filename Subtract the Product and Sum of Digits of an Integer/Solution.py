class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        summ=0
        while(n>0):
            lastNumber=int
            lastNumber=n%10
            product=product*lastNumber
            summ=summ+lastNumber
            n=n//10
        return (product-summ)