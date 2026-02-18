
# class Solution:
#     def isPalindrome(x: int) -> bool:
#         revers = list(str(x))
#         revers.reverse()
        
#         if list(str(x)) == revers:
#             return True
#         else:
#             return False

class Solution:
    def isPalindrome(x: int) -> bool:
        
        if (x - x) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    print(Solution.isPalindrome(x=1222))