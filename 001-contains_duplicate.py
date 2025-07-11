"""
Has Duplicate 
https://leetcode.com/problems/contains-duplicate/description/

Problem description :
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = set()

        for i in nums:
            if i in arr:
                return True
            arr.add(i)
        return False

    print(hasDuplicate([1,2,3,1,1]))