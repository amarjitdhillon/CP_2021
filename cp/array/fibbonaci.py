def fib(n):
    if n > 0:
        if n == 1 or n == 2:
            result = 1
        else:
            result = fib(n-1) + fib(n-2)
    else:
        result = 0  #for handling the -ve numbers
    return result

if __name__ == '__main__':
    result = 0
    number = int(input("Enter the index of fib which you want to see "))
    print('fib for {}th index is {}'.format(number,fib(number)))
