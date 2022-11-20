class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack_list = []
        op_set = {'+', '-', '*', '/'}
        for token in tokens:
            if token not in op_set:
                stack_list.append(int(token))
            else:
                x, y = stack_list.pop(), stack_list.pop()
                stack_list.append(
                    int(eval(f'{y} {token} {x}'))
                )
        return stack_list.pop()


s = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
ss = Solution()
print(ss.evalRPN(s))