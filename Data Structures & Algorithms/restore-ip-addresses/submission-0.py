class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res
        def dfs(i, dots, curIP):
            if i == len(s) and dots == 4:
                res.append(curIP[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) > 256 or (len(s[i:j+1]) > 1 and s[i:j+1][0] == "0"):
                    continue
                dfs(j+1, dots+1, curIP + s[i:j+1] + ".")
        dfs(0, 0, "")
        return res
        