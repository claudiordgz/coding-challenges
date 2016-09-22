'''
For i3.txt
assume
cat1- 1->3->1->2->6=46*2+881+114=1087 cat1 buys 2,1,4 fish types.
cat2- 1->5->1->2->6=997*2+881+114=2989 cat2 buys only remaining fish type
    which is 3 but second cat also have to complete its path to last node.
'''
from fixture import get_testcase

def solution(data):
    pass

def main():
    for t in '0123456789':
        i, o = get_testcase(t)
        print(solution(i) == int(o[0]))

if __name__ == '__main__':
    main()
