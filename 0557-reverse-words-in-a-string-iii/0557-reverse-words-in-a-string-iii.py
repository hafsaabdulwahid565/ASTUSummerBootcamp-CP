class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        y=[]
        for i in range(len(words)):
            r=words[i]
            Rwords=r[::-1]
            y.append(Rwords)
            
        return " ".join(y)

        