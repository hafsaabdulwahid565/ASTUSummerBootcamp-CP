
class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        max_length = 0
        for l in range(len(nums)):
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                r = l
                while r + 1 < len(nums) and nums[r+1] <= threshold and nums[r] % 2 != nums[r+1] % 2:
                    r += 1
                
                current_length = r - l + 1
                if current_length > max_length:
                    max_length = current_length
                    
        return max_length
                    
        
    