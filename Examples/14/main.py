import unittest
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ...

class UnitTest(unittest.TestCase):
    def test_longestCommonPrefix(self):
        long = Solution()
        
        long.longestCommonPrefix(["flower","flow","flight"], "fl")
        long.longestCommonPrefix(["dog","racecar","car"], "")