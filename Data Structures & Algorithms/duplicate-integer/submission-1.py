class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_nums = set()
        for i in nums:
            if i not in distinct_nums:
                distinct_nums.add(i)
            else:
                return True
        return False