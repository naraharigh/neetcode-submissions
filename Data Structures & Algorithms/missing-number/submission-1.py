class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums and len(nums) > 0  :
            if nums[0] != 0:
                return 0
            for i,v in enumerate(nums):
                if i < len(nums) -1:
                    if nums[i+1] - v == 2 :

                        return v+1
        return len(nums)
        