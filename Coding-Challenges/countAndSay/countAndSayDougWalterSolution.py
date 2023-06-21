

def countAndSay(iters: int) -> str:
    if iters < 2:
        return '1'
    lastIter = countAndSay(iters - 1)
    currentChar = lastIter[0]
    currentCharCount = 1
    sequenceTuples = []
    for i in range(len(lastIter)):
        a = lastIter[i]
        if i < len(lastIter) - 1:
            b = lastIter[i + 1]
            if a != b:
                sequenceTuples.append((currentCharCount, currentChar))
                currentChar = b
                currentCharCount = 1
            else:
                currentCharCount += 1
        else:
            sequenceTuples.append((currentCharCount, currentChar))
    outString = ''
    for count, numberChar in sequenceTuples:
        outString += f'{count}{numberChar}'
    return outString



for value, expected in [
    (1, '1'),
    (2, '11'),
    (3, '21'),
    (4, '1211'),
    (5, '111221'),
    (6, '312211')
]:
    print(f"countAndSay({value}): '{countAndSay(value)}', expected: '{expected}'")
    result = countAndSay(value) == expected
    assert result