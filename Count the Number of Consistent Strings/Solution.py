class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        chars = set()
        for i in allowed:
            chars.add(i)
        result = 0
        miss = 0
        for i in words:
            for k in i:
                if k not in chars:
                    miss += 1
                    break
            
        return len(words) - miss