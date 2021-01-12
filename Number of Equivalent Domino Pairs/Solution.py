class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        hasht = dict()
        for i in dominoes:
            if tuple(sorted(i)) in hasht:
                hasht[tuple(sorted(i))] += 1
            else:
                hasht[tuple(sorted(i))] = 1
        count = 0
        for i in hasht:
            if hasht[i] > 2:
#                 I calculated the C(hasht[i], 2) to find exact amount of pair in case of hasht[i] > 2.
                count += int(math.factorial(hasht[i])/(math.factorial(hasht[i] - 2)*2))
            if hasht[i] == 2:
                count += 1
        return count
            