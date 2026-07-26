class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        for i in range(k):
            if s[i] in "aeiou":
                count+=1
        max_v=count
        for i in range(k,len(s)):
            if s[i] in "aeiou":
                count+=1
            if s[i-k] in "aeiou":
                count-=1
            max_v=max(max_v,count)
            if max_v == k:
                return k

        return max_v

        