class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalSum = sum(matchsticks)
        if totalSum %4 != 0:
            return False
        target = totalSum//4
        matchsticks.sort(reverse=True)

        sides = [0] * 4

        def backtrack(i):
            if i == len(matchsticks):
                return True
            for s in range(4):
                if sides[s] + matchsticks[i] <= target:
                    sides[s] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[s] -= matchsticks[i]
            return False
        return backtrack(0)