

def arrayFlatten(arr):
    if len(arr) == 0 or arr is None:
        return arr
    outArr = []
    for elem in arr:
        if type(elem) is list:
            outArr.extend(arrayFlatten(elem))
        else:
            outArr.append(elem)
    return outArr


for caseTuple in [
    ([], []), 
    ([1], [1]), 
    ([1, 2, 3, [1, 2, [3, 4]]], [1, 2, 3, 1, 2, 3, 4])
]:
    testval = arrayFlatten(caseTuple[0]) == caseTuple[1]
    #tempEq = '==' if testval else '!='
    #print(f"arrayFlatten({caseTuple[0]}) {tempEq} {caseTuple[1]}")
    assert testval
