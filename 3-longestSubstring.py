class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        for i in range(len(s)):
            map = {}
            count = 0
            currentString = ""
            for j in range(i,len(s)):
                if s[j] not in map:
                    map[s[j]] = True
                    currentString += s[j]
                    count+=1
                    if count>max:
                        max = count
                else: 
                    break
            print(currentString)
        return max

soluce = Solution()


print(soluce.lengthOfLongestSubstring("dverdreaidf"))

