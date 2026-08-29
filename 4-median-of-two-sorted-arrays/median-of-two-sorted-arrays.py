class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        marged = sorted(nums1 + nums2)
        n = len(marged)
        if n % 2 != 0:
            return float(marged[n//2])
        else:
            mid1 = marged[(n//2)-1]
            mid2 = marged[(n//2)]
            return (mid1 + mid2 ) / 2.0
