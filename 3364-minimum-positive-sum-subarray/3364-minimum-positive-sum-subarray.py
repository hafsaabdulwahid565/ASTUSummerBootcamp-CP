class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        for size in range(l, r + 1):
            x = []
            for i in range(size):
                x.append(nums[i])
            if sum(x) > 0:
                ans = min(ans, sum(x))

            for i in range(size, len(nums)):
                x.pop(0)
                x.append(nums[i])

                if sum(x) > 0:
                    ans = min(ans, sum(x))

        if ans == float('inf'):
            return -1

        return ans