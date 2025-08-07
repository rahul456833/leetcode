class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        dp=[0] *(n*2)
        for i in range(n):
            dp[2*i] = nums[i]
            dp[2*i + 1] = nums[i+n]
        return dp
