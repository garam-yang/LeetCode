class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if stack:
                if stack[-1] == '(' and i ==')':
                    stack.pop()
                elif stack[-1] == '{' and i =='}':
                    stack.pop()
                elif stack[-1] == '[' and i ==']':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        
        if stack:
            return False
        else: 
            return True