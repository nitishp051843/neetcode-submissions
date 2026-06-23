class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixprod = [1]
        postfixprod = [1]
        for i in range(1,len(nums)):
            prefixprod.append(nums[i-1] * prefixprod[i-1])
            postfixprod = [nums[-i] * postfixprod[-i]] + postfixprod
        result = []
        for i in range(len(nums)):
            result.append(prefixprod[i] * postfixprod[i])
        return result
