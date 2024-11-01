"""


"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a, b = int(a), int(b)
        s = a + b
        co = 0

        sum = ''
        while s > 0:
            r = s % 10
            if r + co == 2:
                sum = '0' + sum
                co = 1
            elif r + co == 3:
                sum = '1' + sum
                co = 1
            else:
                sum = str(r + co) + sum
                co = 0
            s = s // 10
        sum = str(co) + sum
        # Drop trailing zero
        if len(sum) > 1 and sum[0] == '0':
            sum = sum[1:]
        return sum
    
    
    
def main():
    s = Solution()
    
    print(s.addBinary('11', '1')) # output: "100"
    print(s.addBinary('1010', '1011')) # output: "10101"
    print(s.addBinary('0', '1')) # output: '1'
    print(s.addBinary('0', '0')) # output: ''
    print(s.addBinary('0', '1')) # output: '1'
    
    
    
import os
if __name__ == "__main__":
    os.system('cls')
    main()