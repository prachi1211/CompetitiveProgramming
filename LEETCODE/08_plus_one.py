class Solution:
    def plusOne(self, li: List[int]) -> List[int]:
        
        s=list(str(int(''.join([str(i) for i in li]))+1))
        for i in range(len(s)):
            s[i]=int(s[i])
        return s    