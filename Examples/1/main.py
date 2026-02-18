from typing import List

class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        count_i = 0
        for i in nums:
            count_j = 0
            for j in nums:
                if count_j != count_i:
                    if (i + j) == target:
                        result = []
                        result.append(count_i)
                        result.append(count_j)
                count_j += 1
            count_i += 1

if __name__ == "__main__":
    Solution.twoSum(nums=[2,7,11,15], target=9) # [0, 1]
    Solution.twoSum(nums=[3, 2, 4], target=6) # [1, 2]
    Solution.twoSum(nums=[3, 3], target=6) # [0, 1]