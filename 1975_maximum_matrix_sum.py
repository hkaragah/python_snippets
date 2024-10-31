"""
GREEDY ALGORITHM:


You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

Example 1:


Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
Example 2:


Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
 

Constraints:

n == matrix.length == matrix[i].length
2 <= n <= 250
-105 <= matrix[i][j] <= 105
"""

class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        """Greedy Strategy:

            Total Absolute Sum: First, calculate the total sum of all elements' absolute
            values. This will be the theoretical maximum if all elements were positive.
            Count Negative Elements: Determine if the matrix has an even or odd number of
            negative elements.
            
            If even: We can make all elements positive, so the sum is simply the total of
            absolute values.
            
            If odd: One element must remain negative because flipping pairs of adjacent
            elements can only affect an even number of elements. To maximize the sum, 
            we leave the smallest absolute value as negative (minimizing the loss) 
            and sum all other absolute values.
            
            Time Complexity: O(n^2) because we iterate through each element once to
            compute the total absolute sum, count negatives, and find the minimum 
            absolute value
        """

        total_sum = 0
        min_value = float('inf')
        negative_count = 0
        
        for row in matrix:
            for value in row:
                # Add the absolute value of each element to the total sum
                total_sum += abs(value)
                # Track the smallest absolute value
                min_value = min(min_value, abs(value))
                # Count negative numbers
                if value < 0:
                    negative_count += 1
        
        # If the number of negatives is even, all can be made positive
        if negative_count % 2 == 0:
            return total_sum
        else:
            # If odd, leave the smallest absolute value negative
            return total_sum - 2 * min_value





def main():
    s = Solution()
    
    print(s.maxMatrixSum([[1,-1],[-1,1]])) # output: 4
    print(s.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]])) # output: 16
    print(s.maxMatrixSum([[-1,0,-1],[-2,1,3],[3,2,2]])) # output: 15
    print(s.maxMatrixSum([[2,9,3],[5,4,-4],[1,7,1]])) # output: 34
    
import os
if __name__ == "__main__":
    os.system('cls')
    main()