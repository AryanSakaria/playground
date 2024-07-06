class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l, n = 0, len(tokens)
        stack = []
        while l < n:
            if tokens[l] == '*':
                b = int(stack[-1])
                stack.pop()
                a = int(stack[-1])
                stack.pop()
                ans = a * b
                stack.append(int(ans))
            elif tokens[l] == '-':
                b = int(stack[-1])
                stack.pop()
                a = int(stack[-1])
                stack.pop()
                ans = a - b
                stack.append(int(ans))
            elif tokens[l] == '+':
                b = int(stack[-1])
                stack.pop()
                a = int(stack[-1])
                stack.pop()
                ans = a + b
                stack.append(int(ans))
            elif tokens[l] == '/':
                b = int(stack[-1])
                stack.pop()
                a = int(stack[-1])
                stack.pop()
                ans = a / b
                stack.append(int(ans))
            else:
                stack.append(int(tokens[l]))
            l+=1
        return stack[-1]
