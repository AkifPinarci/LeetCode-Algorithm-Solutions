class Solution:
    def defangIPaddr(self, address: str) -> str:
        newadress=str
        newadress=address.replace(".","[.]")
        return newadress