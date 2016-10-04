import re

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

'''

'''

from enum import Enum

class State(Enum):
    multiply = 1
    power = 2
    none = 3


def get_element(op, i, expression):
    c = expression[i]
    to_push = ''
    while op(c):
        to_push += c
        i += 1
        if (i >= len(expression)):
            break
        c = expression[i]
    return to_push, i


def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number


def the_pow(x, y):
    return pow_mod(x,y,1000000007)

def solution(elements):
    if not elements or elements[0] == '*' or elements[-1] == '*':
        raise SyntaxError('first OR last element can\'t be *')
    else:
        states = State.none
        stack = []
        processingOp = False
        i = 0
        while i < len(elements):
            c = elements[i]
            if is_number(c):
                if c == '0' and not processingOp:
                    raise SyntaxError('first number can\'t be 0')
                latest_element, i = get_element(is_number, i, elements)
                if states == State.power:
                    previous = stack.pop()
                    stack.append(the_pow(int(previous),int(latest_element)))
                else:
                    stack.append(latest_element)
            else:
                op, i = get_element(lambda x: not is_number(x), i, elements)
                opN = len(op)
                if opN > 2:
                    raise SyntaxError('{n} is not a valid operator'.format(n=op))
                elif opN == 2:
                    states = State.power
                else:
                    states = State.multiply
        acc = int(stack.pop())
        while stack:
            n = int(stack.pop())
            acc = acc * n
        return acc


def main():
    expressions = ['1**2**1**3**2**3*2**1**2**3**2*2','99999999999999999**99999999999999999', '999999999**9999999999999*100','3*2**3**2*5', '2**4*5**3', '3***4', '*2**3', '2***3', '4*5**', '4**2*']
    # data = [l.rstrip('\n') for l in fileinput.input()]
    # n = int(data[0])
    # expressions = data[1:]
    for exp in expressions:
        try:
            print(solution(exp))
        except SyntaxError:
            print('Syntax Error')


if __name__ == '__main__':
    main()


