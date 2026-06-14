class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        y={}
        for i in strs:
            x="".join(sorted(i))
            if x not in y:
                y[x]=[] 
            y[x].append(i)
        return list(y.values())


        