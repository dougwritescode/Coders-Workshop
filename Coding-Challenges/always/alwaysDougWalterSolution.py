

class always:

    def __init__(self, input: str):
        self._value = input

    def __call__(self):
        return self._value


for caseString in ['apple', 'pear', '']:
    case = always(caseString)
    assert case() == caseString