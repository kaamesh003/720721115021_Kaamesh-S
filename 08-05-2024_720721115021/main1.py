def romanToInt(s: str) -> int:
    result = 0
    for i in range(len(s)):
        if i > 0 and get_value(s[i]) > get_value(s[i-1]):
            result += get_value(s[i]) - 2 * get_value(s[i-1])
        else:
            result += get_value(s[i])
    return result

def get_value(c: str) -> int:
    if c == 'I':
        return 1
    elif c == 'V':
        return 5
    elif c == 'X':
        return 10
    elif c == 'L':
        return 50
    elif c == 'C':
        return 100
    elif c == 'D':
        return 500
    elif c == 'M':
        return 1000
    else:
        raise ValueError("Invalid character")
print("use Case 1")
print(romanToInt("III"))
print("Use Case 2")
print(romanToInt("LVIII"))
print("Use Case 3")
print(romanToInt("MCMXCIV"))