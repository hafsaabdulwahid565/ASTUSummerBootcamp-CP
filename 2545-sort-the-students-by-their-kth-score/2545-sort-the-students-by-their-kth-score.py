class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda x:x[k],reverse=True)
        y=[]
        for i in range(len(score)):
             x=[]
             for j in range(len(score[0])):
                 x.append(score[i][j])
             y.append(x)
            
        return y

        
        