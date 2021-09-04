class Solution:
    def isPalindrome(self, name: str) -> bool:
        name = (''.join(filter(str.isalnum,name))).lower()
        if name == name[::-1]:
            return True
        return False