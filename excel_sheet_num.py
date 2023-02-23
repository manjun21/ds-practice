def titleToNumber(columnTitle: str) -> int:
    output = 0
    pos = 0
    for l in reversed(columnTitle):
        print(ord(l))
        digit = ord(l) - 64
        output = output + digit * 26 ** pos
        pos = pos +1

titleToNumber("AB")