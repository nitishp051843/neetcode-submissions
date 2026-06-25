class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        distinct_nums = set(nums)

        return 2 * sum(distinct_nums) - sum(nums)