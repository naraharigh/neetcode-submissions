class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                sub_str = ""
                while stack[-1] != '[':
                    sub_str = stack.pop() + sub_str
                stack.pop()
                
                num_str = ""
                while stack and stack[-1].isdigit():
                    num_str = stack.pop() + num_str
                
                stack.append(sub_str * int(num_str))
            else:
                stack.append(c)
        return ''.join(stack)