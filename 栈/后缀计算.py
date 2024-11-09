from stack import Stack


def hou_calc(exp):
    s = Stack()
    for i in exp:
        if i.isdigit():
            s.push(i)
        else:
            a = s.pop()
            b = s.pop()
            s.push(str(do_math(i, int(b), int(a))))
    return s.pop()


def do_math(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return 0


print(hou_calc("456*7-+"))  # 输出: 5
