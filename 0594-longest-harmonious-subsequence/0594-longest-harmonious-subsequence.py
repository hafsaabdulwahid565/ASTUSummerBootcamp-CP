class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        z=0
        for i in range (len(nums)):
            while nums[i]-nums[left]>1:
                left=left+1
            if nums[i]-nums[left]==1:
                 z=max(z,i-left+1)

        return z

      

        