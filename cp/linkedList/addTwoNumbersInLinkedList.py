"""
2 Add Two Numbers [LeetCode]
a = [2,4,9]
b = [5,6,4,9]
r = [7,0,4,0,1]


Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

def add(a,b):
    la = len(a)
    lb = len(b)
    max_len = max(la, lb)
    res = [0 for i in range(0,max_len)]
    carry = 0
    for i in range(0,max_len):
        if i >= la:
            res[i] =  b[i] + carry
        elif i >= lb :
            res[i] = a[i] + carry
        else:
            res[i] = a[i] + b[i] + carry
        carry = 0               # setting it after the addition is done
        if res[i] > 9:
            sres = str(res[i])
            carry = int(sres[0])
            res[i] = int(sres[1])
    if carry > 0:
        res.append(carry)

    print(res)


if __name__ == '__main__':
    # a = [2,4,9 ]
    # b = [5,6,4,9]

    a = [9,9,9,9,9,9,9]
    b = [9, 9, 9, 9]  # res =  [8,9,9,9,0,0,0,1]
    add(a,b)