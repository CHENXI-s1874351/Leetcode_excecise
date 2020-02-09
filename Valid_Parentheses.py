class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if len(stack) == 0: return False
                if ch == ')':
                    a = stack.pop()
                    if a != '(': return False
                elif ch == ']':
                    a = stack.pop()
                    if a != '[': return False
                elif ch == '}':
                    a = stack.pop()
                    if a != '{': return False
                else:
                    continue
        if len(stack) > 0: return False
        return True
