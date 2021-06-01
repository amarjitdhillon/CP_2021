
def reverseInteger(x):
    # handling the edge case when the x is zero
    if x == 0 :
        return 0

    # take the abs if the value is negative and then handle it at end while returning the result
    if x > 0:
        s = str(x)
    else:
        s = str(abs(x))
    s = s[::-1]

    # we need to return as int
    r = int(s)

    # handle the edge case when output is less then or greater then given constraint
    if r > pow(2,31) or r < pow(-2,31):
        return 0

    # show result based off if the value is positive or negative
    if x >0:
        return r
    else:
        return -r


if __name__ == '__main__':
    x = 123         # 321
    x = 120         # 21
    x = -123        # -321
    x = 1534236469  # 0
    print(reverseInteger(x))