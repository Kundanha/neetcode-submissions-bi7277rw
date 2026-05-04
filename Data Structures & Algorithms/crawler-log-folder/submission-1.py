class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        stack = []
        for l in logs:
            if l == "../": 
                if stack:
                    stack.pop()
                else:
                    continue
            elif l == "./":
                continue
            else:
                stack.append(l)
        return(len(stack))
