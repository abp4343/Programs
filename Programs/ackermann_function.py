def ackermann_fcn (x, y):

    if(x == 0):
        return y + 1

    if(x == 1 and y == 0):
        return 2

    if(x == 1 and y == 1):
        return 3

    if(y == 0):
        return ackermann_fcn(x - 1, 0)

    return ackermann_fcn(x - 1, ackermann_fcn(x, y - 1))