class Solution:
    def maxDistinct(self, s: str) -> int:
        x=set()

        for i in range (len(s)):
            substring =s[i]
            if s[i] not in x:
                x.add(s[i])


        return len(x)



        