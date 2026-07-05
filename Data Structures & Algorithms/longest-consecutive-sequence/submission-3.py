class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 1
        len1 = len(nums)
        i = 0
        j = 1
        if len1  == 0:
            return 0
        nums.sort()
        while(i < len1-1): 

            if len1-1 == i :
                break

            if nums[i] - nums[i+1] == 0 :
                i = i+1
                
                continue

            if abs(nums[i] - nums[i+1]) == 1:
                j +=1 
                maxlen = max(maxlen,j)
                i = i+1 
            else:
                i = i+1
                j = 1

        return maxlen