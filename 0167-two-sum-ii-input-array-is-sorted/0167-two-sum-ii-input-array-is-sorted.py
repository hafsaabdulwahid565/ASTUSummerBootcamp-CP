class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        x=[]
        while left< right:
            if numbers[left]+ numbers[right]==target:
                x.append(left+1)
                x.append(right+1)
                return(x)
            elif numbers[left]+ numbers[right]>target :
                right-=1 

            else:
                left+=1
                
                
         

        