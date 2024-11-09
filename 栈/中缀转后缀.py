from stack import Stack

def infix_to_postfix(infix_expr):
    token_list = infix_expr.split()
    precedence = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    postfix_list = []
    s = Stack()
    for token in token_list:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token.isdigit():
            postfix_list.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            top_token = s.pop()
            while top_token != '(':
                postfix_list.append(top_token)

                top_token = s.pop()
        else:
            while (not s.isEmpty()) and (precedence[s.peek()] >= precedence[token]):
                postfix_list.append(s.pop())
            s.push(token)
    while not s.isEmpty():
        postfix_list.append(s.pop())
    return ' '.join(postfix_list)


print("A+B*(C+D)=",infix_to_postfix("A+B*(C+D)"))