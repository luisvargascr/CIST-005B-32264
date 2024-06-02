# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    x = float(23)
    y = float(23.332)
    print("%.2f" % x)
    print("%.2f" % y)

    for exponent in range(7, 11):
        print("%-3d%12d" % (exponent, 10 ** exponent))

    lyst1 = [1, 3, 4, 5]
    lyst2 = lyst1 # shallow copy
    print(lyst2)

    lyst2 == lyst1
    print(lyst2)

    lyst3 = list(lyst1) # deep copy


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

