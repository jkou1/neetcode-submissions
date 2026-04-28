class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for char in tokens:
            # first few cases can be if we find an operator, 
            # bc that will mean we've seen variables that can be operated on in the stack already

            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            elif char == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif char == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(char))


        return stack[0]