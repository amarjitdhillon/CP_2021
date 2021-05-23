def getRecFraction(n,d):
    a = "" # answer variable
    val = {}
    sign = ""
    if d *n <0:
        sign = "-"
        n = abs(n)
        d = abs(d)
    q = n//d
    r = n%d
    a += str(q) # initial value is added
    if r == 0:
        return sign+a
    else:
        a += str(".")
        while(r != 0):
            if r not in val.keys():
                val[r] = len(a)
            else:
                pos = val[r]
                return sign + a[:pos] + "(" + a[pos:] + ")"
            r = r*10
            q = r//d
            r = r%d
            a += str(q)
        return sign+a


if __name__ == '__main__':
    n = -50
    d = 8
    print(getRecFraction(n,d))