class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total=1
        descent_periods=1
        for i in range(1,len(prices)):
            if prices[i]==prices[i-1]-1:
                descent_periods+=1
            else:
                descent_periods=1
            total+=descent_periods
        return total
        