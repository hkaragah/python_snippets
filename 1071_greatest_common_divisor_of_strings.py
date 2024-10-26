class MySolution(object):
    @staticmethod
    def gcdOfStrings(str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1)<=len(str2):
            short_str, long_str=str1, str2
        else:
            short_str, long_str = str2, str1
        
        divisor = short_str
        
        while len(divisor)>0:
            i = 0
            
            while long_str[i*len(divisor):]!='':
                if long_str[i*len(divisor):(i+1)*len(divisor)]!=divisor:
                    divisor = divisor[:-1]
                    break                  
                else:
                    if  short_str[i*len(divisor):]!='' and short_str[i*len(divisor):(i+1)*len(divisor)]!=divisor:
                        divisor = divisor[:-1]
                        break
                    else:
                        i += 1  
                         
            if long_str[i*len(divisor):]=='': break  
                             
        return divisor

class OtherSolution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])


import os
import unittest

class TestGreatestCommonDivisorOfStrings(unittest.TestCase):
    
    def setUp(self):
        self.word_11 = 'ABCABC'
        self.word_12 = 'ABC'
        
        self.word_21 = 'ABABAB'
        self.word_22 = 'ABAB'
        
        self.word_31 = 'LEET'
        self.word_32 = 'CODE'
        
        self.word_41 = 'ABCDEF'
        self.word_42 = 'ABC'
        
        self.word_51 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
        self.word_52 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"


    def tearDown(self):
        pass
    
    def test_my_solution(self):
        self.assertEqual(MySolution.gcdOfStrings(self.word_11, self.word_12), 'ABC')
        self.assertEqual(MySolution.gcdOfStrings(self.word_21, self.word_22), 'AB')
        self.assertEqual(MySolution.gcdOfStrings(self.word_31, self.word_32), '')
        self.assertEqual(MySolution.gcdOfStrings(self.word_41, self.word_42), '')
        self.assertEqual(MySolution.gcdOfStrings(self.word_51, self.word_52), "TAUXX")
        
        
    def test_other_solution(self):
        self.assertEqual(OtherSolution.gcdOfStrings(self, self.word_11, self.word_12), 'ABC')
        self.assertEqual(OtherSolution.gcdOfStrings(self, self.word_21, self.word_22), 'AB')
        self.assertEqual(OtherSolution.gcdOfStrings(self, self.word_31, self.word_32), '')
        self.assertEqual(OtherSolution.gcdOfStrings(self, self.word_41, self.word_42), '')
        self.assertEqual(OtherSolution.gcdOfStrings(self, self.word_51, self.word_52), "TAUXX")
        
        
        
if __name__ == '__main__':
    os.system('cls') if os.name == 'nt' else os.system('clear')
    unittest.main()  