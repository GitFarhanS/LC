import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)  # truncates toward zero
        }
        
        for char in tokens:
            if char.lstrip('-+').isdigit():  # handles negative and positive
                stack.append(int(char))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[char](a, b))
        
        return stack[0]