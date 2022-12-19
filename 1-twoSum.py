class Solution:
    #time limit on this one 
    def twoSum(self, nums, target: int) :
        outputTab = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                print(i,j)
                if nums[i]+nums[j] == target:
                    outputTab.append(i)
                    outputTab.append(j)
                    return outputTab
        return []
    def twoSum(self,nums,target:int):
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i
            else:
                return map[nums[i]], i
        return None


solution = Solution()
print(solution.twoSum([3,6,2],8))