#LC 88
#sort two sorted arrays in place
#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Merge two sorted arrays nums1 and nums2 into nums1 as one sorted array.
        """
        # Indexes for nums1, nums2, and the end of the merged array
        idx1, idx2, end_idx = m - 1, n - 1, m + n - 1

        # Merge in reverse order
        #use empty space

        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] > nums2[idx2]:
                nums1[end_idx] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[end_idx] = nums2[idx2]
                idx2 -= 1
            end_idx -= 1

        # Copy remaining elements from nums2 if any
        while idx2 >= 0:
            nums1[end_idx] = nums2[idx2]
            idx2 -= 1
            end_idx -= 1