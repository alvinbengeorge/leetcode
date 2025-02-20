class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            if n % 2 == 0:
                return (nums2[n // 2 - 1] + nums2[n // 2]) / 2
            else:
                return nums2[n // 2]
        else:
            half = (m + n + 1) // 2
            left = 0
            right = m
            while True:
                mid1 = left + (right - left) // 2
                mid2 = half - mid1
                if mid1 - 1 >= 0:
                    lower1 = nums1[mid1 - 1]
                else:
                    lower1 = -inf
                if mid1 < m:
                    upper1 = nums1[mid1]
                else:
                    upper1 = inf
                if mid2 - 1 >= 0:
                    lower2 = nums2[mid2 - 1]
                else:
                    lower2 = -inf
                if mid2 < n:
                    upper2 = nums2[mid2]
                else:
                    upper2 = inf
                if lower1 <= upper2 and lower2 <= upper1:
                    break
                elif lower1 > upper2:
                    right = mid1 - 1
                else:
                    left = mid1 + 1
            if (m + n) % 2 == 1:
                return max(lower1, lower2)
            else:
                return (max(lower1, lower2) + min(upper1, upper2)) / 2

        
