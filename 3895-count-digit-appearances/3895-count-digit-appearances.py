class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        times=0
        for i in range (len(nums)):
             x=str(nums[i])
             y=str(digit)
             
             times+=x.count(y)



        return times
        