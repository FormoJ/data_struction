from unicodedata import digit

from stack import Stack

def baseConvert(decNumber, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while decNumber > 0:
        rem = decNumber % base
        s.push(rem)
        decNumber = decNumber // base

    new = ''
    while not s.isEmpty():
        new += digits[s.pop()]
    return new

print(baseConvert(233, 16))