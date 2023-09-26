def isValid(s) -> bool:
    stack = []
    matchDict = {']': '[', '}': '{', ')': '('}  # the key is the left paren, the match is the right
    for c in s:
        if c in '{[(':
            stack.append(c)
        else:
            # c is a right paren
            if not stack:  # the stack is empty, so there is no matching paren for c
                return False
            top = stack.pop()
            if top != matchDict[c]:     # top of stack should hold a right paren. If c isn't the correct match
                return False            # return False

    if stack:
        return False
    else:
        return True


if __name__ == '__main__':
    print(isValid('[]'))
    print(isValid('[['))
    print(isValid('(())'))
    print(isValid('{}[]()({})'))
    print(isValid('{'))
    print(isValid(''))
