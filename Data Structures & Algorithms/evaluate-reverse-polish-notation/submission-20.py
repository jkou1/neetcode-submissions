class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # add items, when we see an operand we pop the items
        # perform the operand, then push the res back to stack

        stack = []

        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                # t is an operand, so pop the two items on stack
                # and perform t on them
                rightOp = stack.pop()
                leftOp = stack.pop()
                if t == "+":
                    stack.append(leftOp + rightOp)
                elif t == "-":
                    stack.append(leftOp - rightOp)
                elif t == "/":
                    stack.append(int(leftOp / rightOp))
                elif t == "*":
                    stack.append(leftOp * rightOp)
        return stack[0]
