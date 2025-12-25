import unittest

test1: int = 1 # answer 22
test2: int = 1000 # answer 1333
test3: int = 3000 # answer 3133

class Solution:
    def nextBeautifulNumber(n: int) -> int:
        result: str = ""
        # print(f"result start = {result}")
        
        for num in str(n):
            x = str(n).count(num)
            result += str(x)
        return int(result)


class UnitTest(unittest.TestCase):
    def test_nextBeautifulNumber(self):
        self.assertEqual(Solution.nextBeautifulNumber(1), 22)
        self.assertEqual(Solution.nextBeautifulNumber(1000), 1333)
        self.assertEqual(Solution.nextBeautifulNumber(3000), 3133)

if __name__ == "__main__":
    unittest.main()