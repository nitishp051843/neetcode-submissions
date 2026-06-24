class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        output = [1] * n

        running = 1
        for i in range(n):
            output[i] = running
            running *= nums[i]
        
        running = 1

        for i in range(n -1 , -1 , -1):
            output[i] *= running
            running *= nums[i]
        
        return output