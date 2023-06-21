

def rgbToHex(R: int, G: int, B: int) -> str:
    outStr = ''
    for v in [R, G, B]:
        if v < 0:
            v = 0
        if v > 255:
            v = 255
        outStr += f'{hex(v)[2:]}'.zfill(2)
    return outStr.upper()


for value, expected in [
    ((150, 5, 22), '960516'),
    ((0, 89, 192), '0059C0'),
    ((-22, 0, 312), '0000FF')
]: 
    result = rgbToHex(*value) == expected
    #print(f"result: '{rgbToHex(*value)}', expected: '{expected}'")
    assert result