
# i = 1
# while i >= 100:
#     print(i)
#     i += 1

row = 1
while row <= 9:
    cow = 1
    while cow <= 9:
        print(row, cow)
        cow += 1
    row += 1


def print_aa():
    '''打印aa'''
    aa = 666
    return aa


getAa = print_aa()
print(getAa)