class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        y=[]
        x=set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                x.add(nums1[i]) 
        for j in x:
            y.append(j)
        return y

            
        