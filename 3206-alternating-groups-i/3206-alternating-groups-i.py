class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        k=len(colors)
        cnt=0

        for right in range(len(colors)):
            if colors[right]!=colors[(right+1) %k] and colors[(right+2) %k]!=colors[(right+1)%k]:
                cnt+=1
        
        return(cnt)

        