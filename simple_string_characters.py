def solve(s):
    result = [0,0,0,0]
    for c in s:
        if str.isupper(c):
            result[0] += 1
        elif str.islower(c):
            result[1] += 1
        elif str.isdigit(c):
            result[2] += 1
        else:
            result[3] += 1

    return result

print(solve("Codewars@codewars123.com"))     
