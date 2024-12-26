def reverse_number(number):

    rev = 0
    sign = 1 if number > 0 else -1
    number *= sign # to make number positive
    while number > 0:
        rev = rev * 10 + number % 10
        number //= 10
    rev *= sign
    return rev

print(reverse_number(-123456))

