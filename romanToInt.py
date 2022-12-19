class Solution:
    def letterToValue(self,s):
        if s == 'I':
            return 1
        if s == 'V':
            return 5
        if s == 'X':
            return 10
        if s == 'L':
            return 50
        if s == 'C':
            return 100
        if s == 'D':
            return 500
        if s == 'M':
            return 1000

    def romanToInt(self,s) -> int:

        lastValue = self.letterToValue(s[len(s)-1])
        somme = lastValue

        for i in range(len(s)-2,-1,-1):
            
            letterValue = self.letterToValue(s[i])
            if letterValue >= lastValue:
                somme+= letterValue
                lastValue = letterValue
            else:
                somme-= letterValue
                lastValue = letterValue
        
        return somme

solution = Solution()
print(solution.romanToInt("VIV"))
            

    