import unittest

# Найти все простые числа меньше или равные заданному числу N.

class Solution:
    def findSimple(n: int) -> dict | None:
        if n <= 1:
            return None
        
        simples: dict = []
        
        for i in range(n):
            
            ...


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution.findSimple(n = 1), None)
    
    def test_11(self):
        self.assertEqual(Solution.findSimple(n = 11), [2, 3, 5, 7, 11])
    
    def test_112(self):
        self.assertEqual(Solution.findSimple(n = 112), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109])
    
    

if __name__ == "__main__":
    unittest.main()

# Найти наибольший общий делитель всех чисел в заданном диапазоне [L, R].