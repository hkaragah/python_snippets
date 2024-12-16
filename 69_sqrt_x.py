"""
69. Sqrt(x)


Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
"""
class Solution:
    def mySqrt(self, x: int) -> int:

        def recursiveSqrt(x,low,high): # recursive function using binary search O(nlogn)
            if x == 1: # edge case
                return x
            elif high - low <= 1: # base case
                if high * high <= x:
                    return high
                else:
                    return low
            else: # recursive case
                mid = (low + high) // 2
                if mid*mid > x:
                    return recursiveSqrt(x, low, mid)
                elif mid*mid < x:
                    return recursiveSqrt(x, mid, high)
                else:
                    return mid

        return recursiveSqrt(x, 0, x//2)
    
    
    
def main():
    s = Solution()
    
    print(s.mySqrt(4)) # output: "2"
    print(s.mySqrt(8)) # output: "2"
    print(s.mySqrt(1)) # output: "1"
    print(s.mySqrt(2)) # output: "1"
    print(s.mySqrt(2147395599)) # output: "46339"
    
    
    
import os
if __name__ == "__main__":
    os.system('cls')
    main()