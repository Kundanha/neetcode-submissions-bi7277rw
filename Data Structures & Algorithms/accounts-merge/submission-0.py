class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par = [i  for i in range(len(accounts))]
        rank = [0] * len(accounts)
        emailToAcc = {}
        def find(e):
            if e == par[e]:
                return e
            par[e] = find(par[e])
            return par[e]
        
        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return False
            if rank[pu] > rank[pv]:
                par[pv] = pu
                rank[pu] += rank[pv]
            else:
                par[pu] = pv
                rank[pv] += rank[pu]
            return True
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        print(emailToAcc)
        print(par)
        groupAcc = defaultdict(list)
        for e, i in emailToAcc.items():
            parent = find(i)
            groupAcc[parent].append(e)
        res = []
        for i, emails in groupAcc.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        return res

        