# input a str for example 3 + (5 - 2) * 3
from collections import deque


def calculate(expr: str):
    def _eval(expr_q):
        num = 0
        stack = []
        op = '+'
        while expr_q:
            c = expr_q.popleft()
            if c == '(':
                num = _eval(expr_q)
            elif c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() or not expr_q or c == ')':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    prev = stack.pop()
                    stack.append(prev * num)
                elif op == '/':
                    prev = stack.pop()
                    stack.append(prev / num)
                op = c
                num = 0
            if c == ')':
                return sum(stack)

        return sum(stack)

    expr_q = deque(expr)
    return _eval(expr_q)


print(calculate('3+5-8-2+4+(2+1)*5-(4-1)'))
