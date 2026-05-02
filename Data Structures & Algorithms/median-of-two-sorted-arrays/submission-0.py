class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # [1,2,6],[4,7,9]
        s = sorted(nums1+nums2)
        if len(s)%2 == 0 : return (s[len(s)//2-1]+s[len(s)//2])/2
        else : return s[len(s)//2]