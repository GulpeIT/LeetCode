import unittest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        revers = list(str(x))
        revers.reverse()
        
        if list(str(x)) == revers:
            return True
        else:
            return False

class UnitTest(unittest.TestCase):
    def test_nextRomanToInt(self):
        s = Solution()
        
        self.assertEqual(s.isPalindrome(121), True)
        self.assertEqual(s.isPalindrome(-121), False)
        self.assertEqual(s.isPalindrome(10), False)

if __name__ == "__main__":
    unittest.main()