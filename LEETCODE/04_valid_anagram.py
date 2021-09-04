class Solution:
    def isAnagram(self, name1: str, name2: str) -> bool:
        if sorted(name1) == sorted(name2):
            if 1<=len(name1)<=(5*pow(10,4)): 
                return True
        else:
            if 1<=len(name1)<=(5*pow(10,4)):
                return False