"""
300: Longest increasing subsequence
Given an integer array nums, return the length of the longest strictly increasing 
subsequence

"""

#O(n^2)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #find a way to visualize examples
        #dag
        #subproblem: LIS[k] longest increasing subsequence at index k
        #find relationships among subproblems
        #Lis[k] = 1 + Lis[k-1]
        #generalize the relationship
        #solve subproblems in order

        #LIS[n] = 1 + max(LIS[k] | k < n, A[k] < A[n])

        L = [1] * len(nums)
        for i in range(1, len(L)):
            subproblems = [L[k] for k in range(i) if nums[k] < nums[i]]
            if subproblems:  # Check if subproblems is non-empty
                L[i] = 1 + max(subproblems)
            else:
                L[i] = 1  # If no valid subproblems, LIS length is 1 (the element itself)
        return max(L, default=0) if hasattr(max, 'default') else max(L) if L else 0

      
#this can also be done in O(nlogn) with binary search

#if you want to actually get the longest sequence, keep track of the indices