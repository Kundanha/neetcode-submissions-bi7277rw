class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4
        sides = [0] * 4
        if sum(matchsticks)/4 != length:
            return False
        matchsticks.sort(reverse=True)
        def dfs(i):
            if i == len(matchsticks):
                return True
            for side in range(4):
                if sides[side] + matchsticks[i] <= length:
                    sides[side] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[side] -= matchsticks[i]
            return False
        return dfs(0)
