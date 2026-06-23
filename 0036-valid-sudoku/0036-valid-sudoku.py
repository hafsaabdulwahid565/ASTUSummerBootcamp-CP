class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x = set()  
        
        for i in range(9):  
            for j in range(9):  
                y = board[i][j]
                if y != ".":
                    row = (y, i, "row")
                    col = (y, j, "col")
                    box = (y, i // 3, j // 3, "box")
                    
                    if row in x or col in x or box in x:
                        return False  
                    
                    x.add(row)  
                    x.add(col)
                    x.add(box)
                    
        return True  
