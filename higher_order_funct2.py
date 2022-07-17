def divisor(x):
    def dividend(y):
        return y / x
    return dividend     # here we are returning reference of dividend


divide = divisor(2)
print(divide(10))   # divide has the reference of dividend so the dividend function will get call
