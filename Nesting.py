def check_nesting(nest):
    """
    Given a string that can only contain (){} or [] characters, returns 1 if string is correctly nested, otherwise 0
    """
    brackets = {'[': ']', '(': ')', '{': '}'}
    open_brackets = []
    for b in nest:
        if b in brackets:
            open_brackets.append(b)
        elif open_brackets and brackets[open_brackets[-1]] == b:
            open_brackets.pop(-1)
        else:
            return 0
    if not open_brackets:
        return 1
    else:
        return 0
