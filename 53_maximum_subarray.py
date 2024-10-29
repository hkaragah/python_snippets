"""
DYNAMIC PROGRAMING:

Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution(object):
    def maxSubArray(self, nums, memo={}):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            total = nums[0]
        else:
            try:
                total = memo[tuple(nums)]
            except KeyError:
                sub_total_left, _ = self.maxSubArray(nums[:-1], memo)
                sub_total_right, _ = self.maxSubArray(nums[1:], memo)
                total = sub_total_left + nums[-1]
        memo[tuple(nums)] = total
        return total, memo
    
    def maxSubArray_1(self, nums, memo={}):
        """
        :type nums: List[int]
        :rtype: int
        """

        def subTotal(nums, memo):
            if len(nums)==1:
                total = nums[0]
            else:
                try:
                    total = memo[tuple(nums)]
                except KeyError:
                    sub_total_left = subTotal(nums[:-1], memo)
                    sub_total_right = subTotal(nums[1:], memo)
                    total = sub_total_left + nums[-1]
            memo[tuple(nums)] = total
            return total

        _ = subTotal(nums, memo)
        return max(memo.values())
    
    
def main():
    s = Solution()
    
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray_1(nums, memo={})) # Expected output = 6 (The subarray [4,-1,2,1] has the largest sum 6.)

            
    nums = [1]
    print(s.maxSubArray_1(nums, memo={})) # Expected output = 1 (The subarray [1] has the largest sum 1.)
    
    nums = [5,4,-1,7,8]
    print(s.maxSubArray_1(nums, memo={})) # Expected output = 23 (The subarray [5,4,-1,7,8] has the largest sum 23.)


import os    
    
if __name__=='__main__':
    os.system('cls') if os.name == 'nt' else os.system('clear')
    main()