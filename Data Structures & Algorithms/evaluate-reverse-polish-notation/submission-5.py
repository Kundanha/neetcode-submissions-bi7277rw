class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = "+-*/"

        for token in tokens:
            if token not in op:
                stack.append(int(token))
            else:
                sec = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first + sec)
                elif token == "-":
                    stack.append(first - sec)
                elif token == "*":
                    stack.append(first * sec)
                elif token == "/":
                    stack.append(int(first / sec))
        return stack[-1]


        