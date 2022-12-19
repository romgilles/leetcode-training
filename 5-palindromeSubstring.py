class Solution:
    def longestPalindrome(self,s):
        startIndex = 0
        endIndex = 0
        maxPal = 0

        for i in range(len(s)):

            len1 = 0
            len1 = self.expandFromMiddle(s,i,i+1)
            len2 = self.expandFromMiddle(s,i,i)
            
            currentLength = max(len1,len2)
            
            if(currentLength>maxPal):
                #palindrome classique abba
                if(currentLength == len1):
                    startIndex = i - currentLength // 2 
                    endIndex = i + currentLength //2 
                #palindrome impair kayak
                else:
                    startIndex = i - currentLength // 2 
                    endIndex = i + currentLength // 2 + 1
                maxPal = currentLength

        return s[startIndex:endIndex+1]



    def expandFromMiddle(self,s,left,right):

        while(left>= 0 and right < len(s) and s[left]==s[right]):
            left-=1
            right+=1

        return right - left - 1


soluce = Solution()
print(soluce.longestPalindrome("kayak"))

#kayakayak