class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge = trust[0][1]
        for mem in trust:
            if judge != mem[1]:
                return -1
        return judge

        