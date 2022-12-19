class Solution:
    def myAtoi(self, s: str) -> int:

        return int(self.extractNumber(s))

    def extractNumber(self,s):
        number= ""
        for i in range(len(s)):
            if s[i].isdigit():
                number+=s[i]
            if number != "" and not s[i].isdigit():
                return number
        return number

soluce = Solution()
print(soluce.myAtoi("-4222"))