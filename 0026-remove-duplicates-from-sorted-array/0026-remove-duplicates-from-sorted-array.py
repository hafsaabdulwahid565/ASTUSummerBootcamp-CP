class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=set(nums)
        nums[:]=sorted((list(k)))
        return len(nums)

        

    
       # for i in range (len(nums)):

        
        

        