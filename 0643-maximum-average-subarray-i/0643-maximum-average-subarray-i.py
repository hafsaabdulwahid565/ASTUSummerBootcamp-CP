class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum=0
        max_a=0
        for i in range(k):
            current_sum+=nums[i]
        max_a=current_sum
        
        l=0
        for i in range(k,len(nums)):
            current_sum+=nums[i]
            current_sum-=nums[l]
            max_a=max(current_sum,max_a)
            l+=1
        return max_a/k

