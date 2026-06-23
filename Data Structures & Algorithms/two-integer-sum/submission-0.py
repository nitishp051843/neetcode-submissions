class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for ind, i in enumerate(nums):
            if i not in diff:
                diff[target - i] = ind
            else:
                return [diff[i], ind]
