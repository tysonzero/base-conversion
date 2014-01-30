import math

digits = {
    0:'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
}

def setDigits(value, base=0):
    if base < 0 or base == 1:
        raise ValueError, 'Base must be an integer greater than or equal to 2 or 0 to set default.'
    digits[base] = str(value)

def convert(value, initial, terminal):
    return fromNumber(toNumber(value, initial), terminal)

def toNumber(value, base):
    if int(base) < 2 or int(base) != base:
        raise ValueError, 'Base must be an integer greater than or equal to 2.'

    value = str(value)

    decimal = value.find('.')

    value = value.replace('.', '')

    if (decimal == -1):
        i = len(value)
    else:
        i = decimal

    number = 0
    b = 0

    if digits.get(base, ''):
        b = base 

    for char in value:
        i -= 1

        if digits[b].find(char) != -1 and digits[b].find(char) < base:
            number += digits[b].find(char) * base**i

    return number


def fromNumber(number, base):
    if int(base) < 2 or int(base) != base:
        raise ValueError, 'Base must be an integer greater than or equal to 2.'

    value = ''
    i = 0
    b = 0

    if digits.get(base, ''):
        b = base 

    try:
        for i in reversed(xrange(1 + int(round(math.log(number, base), 10)))):
            x = int(number / base**i)
            number -= x * base**i
            value += digits[b][x]
    except ValueError:
        value = '0'

    return value