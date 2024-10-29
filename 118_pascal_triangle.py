class Solution(object):
    
    def generate_recursive(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            t = self.generate_recursive(numRows - 1)
            t.append([1] * numRows)
            for i in range(1, numRows-1):
                t[-1][i] = t[-2][i] + t[-2][i-1]
            return t
        
    def generate_buttom_up(self, numRows):
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            t = [[1],[1,1]]
            for i in range(3, numRows+1):
                t.append([1] * i)
                for j in range(1, i-1):
                    t[-1][j] = t[-2][j] + t[-2][j-1]
            return t
      
        
def main():
    s = Solution()
    print(s.generate_buttom_up(5))
        
import os
import unittest


class TestPascalTriangle(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
        
        self.numRows1 = 5
        self.ans1 = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        
        self.numRows2 = 1
        self.ans2 = [[1]]

    def tearDown(self):
        pass
    
    def test_generate_recursive(self):
        self.assertEqual(self.solution.generate_recursive(self.numRows1), self.ans1)
        self.assertEqual(self.solution.generate_recursive(self.numRows2), self.ans2)

    def test_generate_buttom_up(self):
        self.assertEqual(self.solution.generate_buttom_up(self.numRows1), self.ans1)
        self.assertEqual(self.solution.generate_buttom_up(self.numRows2), self.ans2)
        
        
        
if __name__ == '__main__':
    os.system('cls') if os.name == 'nt' else os.system('clear')
    unittest.main()
    # main()