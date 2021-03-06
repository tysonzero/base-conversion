digit_strings = {
    0: '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
}


separators = {
    0: '.',
}


def int_log(number, base):
    i = 0
    while base**i <= number:
        i += 1
    return i - 1


def set_digits(value, base=0):
    digit_strings[int(base)] = str(value)


def set_separators(value, base=0):
    separators[int(base)] = str(value)


def to_number(value, base):
    value = str(value)
    base = int(base)
    digit_string = digit_strings.get(base) or digit_strings[0]
    separator = separators.get(base) or separators[0]
    decimal = value.find(separator)
    decimal = len(value) - 1 if decimal == -1 else decimal - 1
    value = value.replace(separator, '')
    number = 0
    for i, char in enumerate(value):
        if digit_string.find(char) != -1 and digit_string.find(char) < base:
            number += digit_string.find(char) * base**(decimal - i)
    return number


def to_base(number, base, precision=0):
    precision = int(precision)
    number = float(number) if precision else int(number)
    base = int(base)
    digit_string = digit_strings.get(base) or digit_strings[0]
    separator = separators.get(base) or separators[0]
    value = ''
    for i in reversed(xrange(precision + 1 + int_log(number, base))):
        x = int(number / base**(i - precision))
        number -= x * base**(i - precision)
        value += digit_string[x]
    if not value:
        value = digit_string[0]
    if precision:
        value = value[:len(value) - precision] + separator + value[len(value) - precision:]
    return value


def convert(value, initial, terminal, precision=0):
    return to_base(to_number(value, initial), terminal, precision)
