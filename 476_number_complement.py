"""
LeetCode Daily Challenge

476. Number Complement

The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

1 <= num < 231
"""
import os

class MySolution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        binary = bin(num).replace('0b','')

        digits = []
        for digit in binary:
            if digit=='0':
                digits.append('1')
            elif digit=='1':
                digits.append('0')

        binary = ''
        for digit in digits:
            binary += digit
        
        num = int(binary, 2)
        return num


class OthersSolution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length() # if num=5 it will be '3'
        
        mask = (1 << bit_length) - 1 # if num=5 it will be '(1 << 3) - 1 = 7'
        
        return num ^ mask # if num=5 it will be '5 ^ 7 = 2'

"""
'number << shift_amount':
    'left shift' operator, it shifts the bits of a number to the left by a specific number
    '5' is binary is 101 with 'bit_length=3'
    '1 << 3' would result in '1000' which is '8' in base 10
    
'num ^ mask':
    is bitwise XOR (exclusive OR) operator andperforms bitwase XOR operation on two integers 'num' and 'maks'
    the result bit is '1' if exactly one of the bits is '1' (but not both). If both are '0' or both are '1', the resulting bit is '0'
    '5 ^ 7' in binary would be '101 XOR 111 = 010' which is 2
"""

def main():
    os.system('cls')
    try:
        num = int(input('Enter a positive integer: '))
    except:
        pass
    else:
        solution = MySolution()
        print(f'{num} complement: {solution.findComplement(num)}')
        
if __name__ == '__main__':
    main()