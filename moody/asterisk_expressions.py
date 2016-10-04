import re

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def reduce_square(elements):
    i, ret = 0, []
    while i < len(elements):
        el = elements[i]
        if not is_number(el):
            n_asterisks = len(el)
            if n_asterisks > 2:
                raise SyntaxError('Operator \'{n}\' does not exist'.format(n=el))
            elif n_asterisks == 2:
                ret[-1] **= int(elements[i + 1])
                i += 2
            else:
                ret.append(elements[i])
                i += 1
        else:
            ret.append(int(elements[i]))
            i += 1
    return ret


def evaluate(elements):
    elements = reduce_square(elements)
    acc = elements[0]
    for n in elements[1:]:
        if is_number(n):
           acc *= n
    return acc


def reduce_sq(elements):
    i, previous = 0, []
    while i < len(elements):
        el = elements[i]
        if not is_number(el):
            n_asterisks = len(el)
            if n_asterisks > 2:
                raise SyntaxError('Operator \'{n}\' does not exist'.format(n=el))
            elif n_asterisks == 2:
                ret[-1] **= int(elements[i + 1])
                i += 2
            else:
                ret.append(elements[i])
                i += 1
        else:
            previous.append(int(elements[i]))
            i += 1


def solution(elements):
    if elements[0] == '*' or elements[-1] == '*':
        raise SyntaxError('first OR last element can\'t be *')
    else:
        reduce_sq(elements)




def main():
    expressions = ['3*2**3**2*5', '2**4*5**3', '3***4', '*2**3', '2***3', '4*5**', '4**2*']
    # data = [l.rstrip('\n') for l in fileinput.input()]
    # n = int(data[0])
    # expressions = data[1:]
    for exp in expressions:
        elements = list(filter(lambda x: x != '', re.split('(\d+)', exp)))
        try:
            print(solution(elements))
        except SyntaxError:
            print('Syntax Error')


if __name__ == '__main__':
    main()


