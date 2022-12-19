class Solution:
    def reverse(self, x: int) -> int:
        intLength = len(str(x))
        sum = 0
        neg = False
        

        if x < 0:
            neg = True
            x= -x
            intLength = intLength-1

        for i in range(1,intLength+1):
            tmp = (x % 10**(i)) // 10**(i-1)
            tmp*= 10**(intLength-i)
            sum += tmp

        if sum > (2**31 -1) or sum < -(2**31):
                return 0

        if neg is True:
            return -sum
        return sum

soluce = Solution()
print(soluce.reverse(1534236469))