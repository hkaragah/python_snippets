""" 
DYNAMIC PROGRAMING:

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""

class Solution(object):
    def climbStairs(self, n, memo={}):
        """ Dynamic Approach
        :type n: int
        :rtype: int
        """
        if n == 1:
            result = 1
        elif n == 2:
            result = 2
        else:
            try:
                result = memo[n]
            except KeyError:
                result = self.climbStairs(n-1) + self.climbStairs(n-2)
        memo[n] = result
        return result
    
    def climbStairs_1(self, n):
        """ Buttom-up Approach
        :type n: int
        :rtype: int
        """
        ans = [0] * n
        ans[1] = 1
        ans[2] = 2
        for i in range(3, n+1):
            ans[i] = ans[i-1] + ans[i-2]
        return ans[n]