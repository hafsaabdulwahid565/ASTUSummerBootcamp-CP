class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
         nums.sort()
         left=0
         right=len(nums)-1
         pairs=0
         while left<right:
            sum=nums[left]+nums[right]
            if sum<target:
                 pairs+=(right-left)
                 left=left+1
            else:
                right=right-1       
         return pairs

        

