class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum=0
        max_sum=0
        for i in range(k):
            current_sum+=nums[i]
        max_sum=current_sum
        l=0
        for j in range(k,len(nums)):
            current_sum+=nums[j]
            current_sum-=nums[l]
            max_sum=max(max_sum,current_sum)
            l+=1
        return max_sum/k
        #1+12-5-6=2
       

            


        