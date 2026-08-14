class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = k
        right = k
        minimum = nums[k]
        answer = nums[k]
        while l > 0 or right < len(nums) - 1:
            if l > 0 and right < len(nums) - 1:
                if nums[l - 1] >= nums[right + 1]:
                    l -= 1
                    minimum = min(minimum, nums[l])
                else:
                    right += 1
                    minimum = min(minimum, nums[right])
            elif l > 0:
                l -= 1
                minimum = min(minimum, nums[l])
            else:
                right += 1
                minimum = min(minimum, nums[right])
            score = minimum * (right - l + 1)
            answer = max(answer, score)

        return answer