class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(','[','{'):
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                elif c==')' and stack[-1]=='(':
                    stack.pop(-1)
                elif c==']' and stack[-1]=='[':
                    stack.pop(-1)
                elif c=='}' and stack[-1]=='{':
                    stack.pop(-1)
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False