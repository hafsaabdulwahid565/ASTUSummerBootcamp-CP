class Solution:
    def minOperations(self, nums: List[int], k: int) :
        operations=0
        
        if sum(nums)%k==0:
             return operations 
        while sum(nums)%k!=0:
                nums[0]=nums[0]-1
                operations=operations +1
        return operations
             




            