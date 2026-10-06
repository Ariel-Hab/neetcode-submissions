from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # The first number popped is the RIGHT operand (b)
                # The second number popped is the LEFT operand (a)
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Python's integer division (//) floors negative numbers (e.g. -1 // 2 = -1).
                    # RPN requires truncating toward zero. int(float) handles this perfectly.
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
                
        # The final result is the only remaining item on the stack
        return stack[0]