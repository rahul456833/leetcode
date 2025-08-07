class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [0] * (2*n)
        for i in range(n):
            dp[i] = nums[i]
            dp[i+n] = nums[i]

        return dp