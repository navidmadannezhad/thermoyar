def anyInputIsEmpty(*values):
    for value in values:
        if bool(value) is False or value == 'what':
            return True
            break
    return False


def inputHasLetter(value):
    try:
        value = float(value)
        return False
    except ValueError:
        return True



