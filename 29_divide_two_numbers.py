class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor:
            return 0

        m1 = divisor
        m2 = divisor + divisor
        q = 1
        while m1 < dividend and m2 < dividend:
            m1 = m1 + m2
            m2 = m2 + m2
            q += 1
        
        if m1 >= dividend:
            return q if sign==1 else -q
        else:
            return q+1 if sign==1 else -(q+1)
        
        
        
def main():
    s = Solution()
    
    print(s.divide(10,3)) # output: 3
    print(s.divide(7,-3)) # output: -2
    
import os
if __name__ == "__main__":
    os.system('cls')
    main()