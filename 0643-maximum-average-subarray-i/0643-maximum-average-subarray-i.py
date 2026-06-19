class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
         x=sum(nums[:k])
         max_sum=x
         for i in range(k,len(nums)):
             x=x+nums[i]-nums[i-k]
             if x>=max_sum:
                 max_sum=x
             

         return max_sum/k
