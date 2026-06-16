
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for i in range(len(matrix[0])):
            r= []
            for j in range(len(matrix)):
                r.append(matrix[j][i])
            transpose.append(r)
        return transpose  
