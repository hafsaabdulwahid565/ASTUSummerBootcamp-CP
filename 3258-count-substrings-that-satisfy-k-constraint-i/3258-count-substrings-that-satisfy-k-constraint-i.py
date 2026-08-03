class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left = 0
        zeros = 0
        ones = 0
        ans = 0
        
        for i in range(len(s)):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            
            while zeros > k and ones > k:
                if s[left] == '0':
                    zeros -= 1
                else:
                    ones -= 1
                left += 1
            
            ans += (i - left + 1)
            
        return ans
        