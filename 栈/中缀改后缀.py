from stack import Stack


def infiToPostfix(exp):
    s = Stack()
    postfix = []
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    for i in exp:
        if i.isalnum():  # 如果是字母或数字
            postfix.append(i)
        elif i == '(':
            s.push(i)
        elif i == ')':
            while s.peek() != '(':
                postfix.append(s.pop())
            s.pop()
        else:
            while s.items and s.peek() != '(' and priority[s.peek()] >= priority[i]:
                postfix.append(s.pop())
            s.push(i)
    while s.items:
        postfix.append(s.pop())
    return ''.join(postfix)


print(infiToPostfix("a+b*c+(d*e+f)*g"))  # 输出: abc*+de*f+g*+
