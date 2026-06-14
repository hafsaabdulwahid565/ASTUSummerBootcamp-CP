class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range (len(nums)):
            x=nums.index
            if nums[i]==target:
                return x(target)
            elif nums[i]>target:
                return i
        return len(nums)
                
        