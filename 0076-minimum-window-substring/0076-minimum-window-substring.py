
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = {}
        for i in t:
            need[i] = need.get(i, 0) + 1
        
        have = {}
        required = len(need)  
        formed = 0    
        
        left = 0
        min_len = float('inf')
        result_start = 0
        for right, i in enumerate(s):
            have[i] = have.get(i, 0) + 1
            
            if i in need and have[i] == need[i]:
                formed += 1
            while formed == required:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    result_start = left
                
                left_char = s[left]
                have[left_char] = have.get(left_char, 0) - 1
                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1
                
                left += 1
        
        return "" if min_len == float('inf') else s[result_start:result_start + min_len]


        
        