
import unittest 

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol: list = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        result = symbol[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            number = symbol[s[i]]
            if symbol[s[i+1]] > number:
                result -= number
            else:
                result += number
        return result





class UnitTest(unittest.TestCase):
    def test_nextRomanToInt(self):
        rom = Solution()
        
        self.assertEqual(rom.romanToInt("III"), 3)
        self.assertEqual(rom.romanToInt("LVIII"), 58)
        self.assertEqual(rom.romanToInt("MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()