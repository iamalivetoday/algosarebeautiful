#Imagine your closet is filled with clothes (represented as the nums array), 
# and some of those clothes are old or torn (represented as the val). 
# You want to remove all the old/torn clothes but still keep the closet organized.


def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k = 0  # Pointer for elements not equal to val
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
