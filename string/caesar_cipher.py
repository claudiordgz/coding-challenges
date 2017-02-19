

def check(c, k):
    min_lower_ascii, max_lower_ascii = ord('a'), ord('z')
    min_upper_ascii, max_upper_ascii = ord('A'), ord('Z')
    def translate(c, k, base):
        pos = c - base
        pos = (pos + k) % 26
        return chr(pos + base)
    
    int_value = ord(c)
    if min_lower_ascii <= int_value <= max_lower_ascii:
        return translate(int_value, k, min_lower_ascii)
    elif min_upper_ascii <= int_value <= max_upper_ascii:
        return translate(int_value, k, min_upper_ascii)
    else:
        return c


def solution(s, k):
    new_str = [check(c, k) for c in s]
    return ''.join(new_str)


def test_fix(s, k, expected):
    r1 = solution(s, k)
    print(r1, r1 == expected)    


def test():
    test_fix('middle-Outz', 2, 'okffng-Qwvb')
    test_fix('www.abc.xy', 87, 'fff.jkl.gh')
    test_fix('159357lcfd', 98, '159357fwzx')
    test_fix('!m-rB`-oN!.W`cLAcVbN/CqSoolII!SImji.!w/`Xu`uZa1TWPRq`uRBtok`xPT`lL-zPTc.BSRIhu..-!.!tcl!-U', 62, '!w-bL`-yX!.G`mVKmFlX/MaCyyvSS!CSwts.!g/`He`eJk1DGZBa`eBLdyu`hZD`vV-jZDm.LCBSre..-!.!dmv!-E')


test()