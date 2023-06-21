from functools import partial


def zero(val: partial|None = None):
    return val(valB=0) if type(val) is partial else 0

def one(val: partial|None = None):
    return val(valB=1) if type(val) is partial else 1

def two(val: partial|None = None):
    return val(valB=2) if type(val) is partial else 2

def three(val: partial|None = None):
    return val(valB=3) if type(val) is partial else 3

def four(val: partial|None = None):
    return val(valB=4) if type(val) is partial else 4

def five(val: partial|None = None):
    return val(valB=5) if type(val) is partial else 5

def six(val: partial|None = None):
    return val(valB=6) if type(val) is partial else 6

def seven(val: partial|None = None):
    return val(valB=7) if type(val) is partial else 7

def eight(val: partial|None = None):
    return val(valB=8) if type(val) is partial else 8

def nine(val: partial|None = None):
    return val(valB=9) if type(val) is partial else 9

def _plusHelper(valA: int, valB: int):
    return valA + valB

def _multHelper(valA: int, valB: int):
    return valA * valB

def _divHelper(valA: int, valB: int):
    return valB // valA

def plus(val: int):
    return partial(_plusHelper, valA=val)

def minus(val: int):
    return partial(_plusHelper, valA=val * -1)

def times(val: int):
    return partial(_multHelper, valA=val)

def divided_by(val: int):
    if val == 0:
        return None
    return partial(_divHelper, valA=val)


#print(f"nine(): {nine()}")
#print(f"plus(nine()): {plus(nine())}")
#print(f"four(plus(nine())): {four(plus(nine()))}")
assert four(plus(nine())) == 13
#print(f"three(): {three()}")
#print(f"minus(three()): {minus(three())}")
#print(f"eight(minus(three())): {eight(minus(three()))}")
assert eight(minus(three())) == 5
#print(f"two(): {two()}")
#print(f"divided_by(two()): {divided_by(two())}")
#print(f"six(divided_by(two())): {six(divided_by(two()))}")
assert six(divided_by(two())) == 3
#print(f"five(): {five()}")
#print(f"times(five()): {times(five())}")
#print(f"seven(times(five())): {seven(times(five()))}")
assert seven(times(five())) == 35
