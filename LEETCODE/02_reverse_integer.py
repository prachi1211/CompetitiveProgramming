class Solution:
    def reverse(self, n: int) -> int:
            name=str(n)
            if name[0] == "-":
                n = int("-" + name[:0:-1])
                if pow(-2,31)<=n<=(pow(2,31)-1):
                    return n
                else:
                    return 0 
            else:
                n = int(name[::-1])
                if pow(-2,31)<=n<=(pow(2,31)-1):
                    return n
                else:
                    return 0