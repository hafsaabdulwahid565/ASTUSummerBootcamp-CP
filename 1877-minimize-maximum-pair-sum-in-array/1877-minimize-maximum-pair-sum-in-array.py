class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        x=0
        right=len(nums)-1
        for i in range(len(nums)//2):
            sum_nums=nums[left]+nums[right]
            left+=1
            right=right-1
            if left==0:
                x=sum_nums
            elif sum_nums>x:
                x=sum_nums
        x=max(x,sum_nums)
        return x



            
        