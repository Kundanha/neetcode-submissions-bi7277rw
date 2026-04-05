class Solution:
    def climbStairs(self, n: int) -> int:
        #res = [0]
        dp = {}
        def backtrack(n):
            if n in dp:
                return dp[n]
            if n < 0:
                return 0
            if n == 0:
                return 1
            onestep = backtrack(n-1)
            twostep = backtrack(n-2)
            dp[n] = onestep + twostep
            return dp[n]
        return backtrack(n)
        