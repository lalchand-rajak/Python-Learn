# def addno(num1, num2):
    # total = num1 + num2
    # return total
def addNo(*num):
    total = 0
    for n in num:
        total = total + n
    return total


print(addNo(3, 3, 3))