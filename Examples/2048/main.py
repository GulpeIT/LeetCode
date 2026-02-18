import unittest

class Solution:
    def nextBeautifulNumber(n: int) -> int:
        result: str = ""
        
        for num in str(n):
            x = str(n).count(num)
            result += str(x)
            if result > n:
                return int(result)  
            else:
                ...


class UnitTest(unittest.TestCase):
    def test_nextBeautifulNumber(self):
        self.assertEqual(Solution.nextBeautifulNumber(1), 22)
        self.assertEqual(Solution.nextBeautifulNumber(1000), 1333)
        self.assertEqual(Solution.nextBeautifulNumber(3000), 3133)

if __name__ == "__main__":
    unittest.main()