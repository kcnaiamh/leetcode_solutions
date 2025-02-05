class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(self, current_stair: int) -> int:
            if current_stair > n:
                return 0
            if current_stair == n:
                return 1
            if current_stair in memo:
                return memo[current_stair]
            memo[current_stair] = dp(self, current_stair + 1) + dp(self, current_stair + 2)
            return memo[current_stair]
        return dp(self, 0)