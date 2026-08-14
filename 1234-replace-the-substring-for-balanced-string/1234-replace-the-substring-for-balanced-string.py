from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        n = len(s)
        target = n // 4
        if all(cnt[c] == target for c in "QWER"):
            return 0

        left = 0
        answer = n

        for right in range(len(s)):
            cnt[s[right]] -= 1
            while ( left<=right and
            cnt["Q"] <= target and
                   cnt["W"] <= target and
                   cnt["E"] <= target and
                   cnt["R"] <= target):
                answer = min(answer, right - left + 1)
                cnt[s[left]] += 1
                left += 1
            

        return answer