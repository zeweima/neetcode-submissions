class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def is_number(c):
            try:
                int(c)
                return True
            except:
                return False
        stack = []
        for c in tokens:
            # print(c, c.isdigit())
            if is_number(c):
                stack.append(int(c))
            else:
                ele2 = stack.pop()
                ele1 = stack.pop()
                if c== '+':
                    stack.append(ele1+ele2)
                elif c=='-':
                    stack.append(ele1-ele2)
                elif c=='*':
                    stack.append(ele1*ele2)
                elif c=='/':
                    stack.append(int(ele1/ele2))
        return stack[0]