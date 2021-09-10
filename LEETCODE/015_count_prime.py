class Solution:
    def countPrimes(self, a: int) -> int:
        count=0
        count_1=0
        if a>2:
            for j in range(2,a):
                for i in range(1,(j+1)):
                    if (j%i)==0:
                        count+=1
                if count>2:
                    count=0
                    pass
                else:
                    count_1+=1
                    count=0
            return count_1 
        else:
            return 0