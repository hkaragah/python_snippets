import unittest
import search
import os

class TestSearch(unittest.TestCase):
    
    def setUp(self) -> None:
        pass
    
    def tearDown(self) -> None:
        pass
    
    def test_binary_search(self):
        sorted_list = [8.25, 22.5 , 35, 48.75, 53.725, 63.05, 71.5, 88.95, 96.6, 105.7, 1024.]
        self.assertEqual(search.binary_search(sorted_list, 35), 2)
        self.assertEqual(search.binary_search(sorted_list, 105.7), 9)
        self.assertEqual(search.binary_search(sorted_list, 100), -1)
        self.assertEqual(search.binary_search(sorted_list, 8.25), 0)
        self.assertEqual(search.binary_search(sorted_list, 1024), len(sorted_list) - 1)
        
        sorted_list1 = [2.5, 5.75, 5.75, 8, 10.5, 12, 17.6, 20] # repeated elements
        self.assertIn(search.binary_search(sorted_list1, 5.75), [1, 2])
        
    def test_binary_search_first_occurence(self):
        sorted_list1 = [2.5, 5.75, 5.75, 8, 10.5, 12, 17.6, 20] # repeated elements
        self.assertEqual(search.binary_search(sorted_list1, 5.75), 1)
        
        sorted_list2 = [-5, -4, -1.5, -1.5, -1.5, 0., 0, 2.25, 3.5, 3.5]
        self.assertEqual(search.binary_search_first_occurence(sorted_list2, -1.5), 2)
        self.assertEqual(search.binary_search_first_occurence(sorted_list2, 0), 5)
        self.assertEqual(search.binary_search_first_occurence(sorted_list2, 3.5), 8)
        

if __name__ == '__main__':
    os.system('cls') if os.name == 'nt' else os.system('clear')
    unittest.main()