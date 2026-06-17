class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left=[]
        right=[]
        between=[]
        y=[]
        x=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                left.append(nums[i])
            elif nums[i]>pivot:
                right.append(nums[i])
            elif nums[i]==pivot:
                between.append(nums[i])

        y.append(left)
        y.append(between)
        y.append(right)
        for i in y:
            x.extend(i)
        return x

        