from stack import Stack

def ParCheck(symbolString):
    s = Stack()
    balance = True  # 是否配对相等
    index = 0  # 循环索引
    while index < len(symbolString) and balance:  # 逐个判断
        symbol = symbolString[index]
        if symbol in "([{":  # 进栈
            s.push(symbol)
        else:
            if s.isEmpty():  # 判断是否为空
                balance = False  # 没有栈顶元素，无法配对
            else:
                top = s.pop()
                if not matches(top, symbol):  # 不匹配
                    balance = False
        index+=1
    if balance and s.isEmpty():  # 循环结束，栈为空，且没有发现不配对情况
        return True
    else:
        return False
def matches(top, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(top) == closers.index(close)


print(ParCheck('{'))
print(ParCheck('[{())))]'))