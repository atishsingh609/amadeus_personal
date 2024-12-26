def check_palindrome(s):
    i = 0

    j = len(s) - 1
    flag = False
    if len(s) == 1 or len(s) == 0:
        return True
    while i < j:
        if s[i] == s[j]:
            flag = True
        else:
            return False
        i = i + 1
        j = j-1

    return flag

print(check_palindrome("raceacar"))