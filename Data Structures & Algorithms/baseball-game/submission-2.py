class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for c in operations:
            if res and c == "+":
                two = res.pop()
                one = res.pop()
                three = one + two
                res.append(one)
                res.append(two)
                res.append(three)
            elif res and c == "D":
                one = res.pop()
                res.append(one)
                res.append(one * 2)
            elif res and c == "C":
                res.pop()
            else:
                res.append(int(c))
        return sum(res)
        