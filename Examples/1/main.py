from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         pass

class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in hashmap:
                return [i, hashmap[num]]
            hashmap[nums[i]] = i

if __name__ == "__main__":
    print(Solution.twoSum([2, 7, 11, 15], 9))