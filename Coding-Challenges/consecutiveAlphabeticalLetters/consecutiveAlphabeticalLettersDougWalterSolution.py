

def consecutiveAlphabetical(instr: str):
    for a, b in zip(instr[:-1], instr[1:]):
        if ord(b) != ord(a) + 1:
            return False
    return True


for value, expected in [
    ('abc', True),
    ('abd', False),
    ('zpe', False),
    ('abcdefghijklmnopqrstuvwxyz', True),
    ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', True)
]:
    assert consecutiveAlphabetical(value) == expected
    print(f"consecutiveAlphabetical('{value}') == {expected}")