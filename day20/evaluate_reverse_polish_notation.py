from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isnumeric() or (token.startswith("-") and len(token) > 1): 
                stack.append(int(token))
            elif token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "/":
                num1, num2 = stack.pop(), stack.pop()   
                stack.append(int(num2 / num1))
            elif token == "*":
                stack.append(stack.pop() * stack.pop())

            else:
                num1, num2 = stack.pop(), stack.pop()   
                stack.append(int(num2 - num1))
        return stack.pop()