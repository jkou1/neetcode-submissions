class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curStack = []

        for token in tokens:
            try:
                # Attempt to convert the token to an integer
                num = int(token)
                curStack.append(num)
            except ValueError:
                # If conversion fails, it must be an operator
                num2 = curStack.pop()
                num1 = curStack.pop()
                if token == "+":
                    curStack.append(num1 + num2)
                elif token == "-":
                    curStack.append(num1 - num2)
                elif token == "*":
                    curStack.append(num1 * num2)
                elif token == "/":
                    # Perform integer division with truncation towards zero
                    result = num1 // num2
                    if result < 0 and num1 % num2 != 0:
                        result += 1
                    curStack.append(result)

        return curStack[0]