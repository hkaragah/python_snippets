"""
35. Search Insert Position


Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
import os
import unittest

class MySolution(object):
    @staticmethod
    def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if mid == right:
                    return mid + 1
                elif nums[mid + 1] > target:
                    return mid + 1
                else:
                    left = mid + 1
            else:
                if mid == left:
                    return mid
                elif nums[mid - 1] < target:
                    return mid
                else:
                    right = mid - 1

class OtherSolution(object):
    @staticmethod
    def searchInsert(nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l
        

class TestSearchInsertPosition(unittest.TestCase):
    def setUp(self):
        self.nums1 = [1, 3, 5, 6]
        self.nums2 = [1, 3, 5, 7]
    
    def tearDown(self):
        pass
    
    def test_my_solution(self):
        self.assertEqual(MySolution.searchInsert(self.nums1, 5), 2)
        self.assertEqual(MySolution.searchInsert(self.nums1, 2), 1)
        self.assertEqual(MySolution.searchInsert(self.nums1, 7), 4)
        self.assertEqual(MySolution.searchInsert(self.nums2, 6), 3)
        self.assertEqual(MySolution.searchInsert(self.nums2, 0), 0)
        
    def test_other_solution(self):
        self.assertEqual(OtherSolution.searchInsert(self.nums1, 5), 2)
        self.assertEqual(OtherSolution.searchInsert(self.nums1, 2), 1)
        self.assertEqual(OtherSolution.searchInsert(self.nums1, 7), 4)
        self.assertEqual(OtherSolution.searchInsert(self.nums2, 6), 3)
        self.assertEqual(OtherSolution.searchInsert(self.nums2, 0), 0)
        
        
if __name__ == '__main__':
    os.system('cls') if os.name == 'nt' else os.system('clear')
    unittest.main()