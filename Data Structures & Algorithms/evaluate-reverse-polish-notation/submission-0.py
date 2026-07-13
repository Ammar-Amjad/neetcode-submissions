class Solution:
    def evalRPN(self, arr: List[str]) -> int:
        Ops = {'+', '-', '/', '*'}
        stack = []
        i  = 0

        for i in range(len(arr)):
            if arr[i] not in Ops:
                stack.append(int(arr[i]))
            else:
                Num2 = stack.pop()
                Num1 = stack.pop()
                Op = arr[i]
                if Op == '+': stack.append(Num1 + Num2)
                elif Op == '-': stack.append(Num1 - Num2)
                elif Op == '/': stack.append(int(Num1 / Num2))
                elif Op == '*': stack.append(Num1 * Num2)
                

        return stack[-1]