class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_l = float("inf")
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_l = min(min_l, right - left + 1)
                current_sum -= nums[left]
                left += 1
        if min_l == float("inf"):
                 return 0

        return min_l
