class MySolution(object):
    
    @staticmethod
    def mergeAlternately(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ''
        len1, len2 = len(word1), len(word2)
        
        for i in range(min(len1, len2)):
            merged = merged + word1[i] + word2[i]
            
        if len1 > len2:
            merged = merged + word1[i+1:]
        elif len2 > len1:
            merged = merged + word2[i+1:]
            
        return merged
            


import os
import unittest

class TestMergeStringsAlternatively(unittest.TestCase):
    
    def setUp(self):
        self.word_11 = 'abcd'
        self.word_12 = 'abc'
        self.word_13 = 'ab'
        
        self.word_21 = 'pq'
        self.word_22 = 'pqr'
        self.word_23 = 'pqrs'

    
    def tearDown(self):
        pass
    
    def test_my_solution(self):
        self.assertEqual(MySolution.mergeAlternately(self.word_12, self.word_22), 'apbqcr')
        self.assertEqual(MySolution.mergeAlternately(self.word_11, self.word_21), 'apbqcd')
        self.assertEqual(MySolution.mergeAlternately(self.word_13, self.word_23), 'apbqrs')
        
        
        
if __name__ == '__main__':
    os.system('cls') if os.name == 'nt' else os.system('clear')
    unittest.main()                