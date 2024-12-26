def check_pali(s, i, j):

    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    else:
        return check_pali(s, i+1, j-1)


def main():
    s = "abcdefedcba"
    j = len(s) -1
    i = 0
    print(check_pali(s, i, j))

main()

