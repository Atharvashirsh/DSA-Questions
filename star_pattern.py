val = 5


def starPattern1(val):
    """

    left align triangle

    *
    **
    ***
    ****
    *****

    """
    for i in range(val):
        for j in range(i + 1):
            print("*", end="")
        print()


def starPattern2(val):
    """
    right align triangle

        *
       **
      ***
     ****
    *****

    """
    for i in range(val):
        for j in range(val - i - 1):
            print(" ", end="")
        for k in range(i + 1):
            print("*", end="")
        print()


def starPattern3(val):
    """
    inverse left align

    *****
    ****
    ***
    **
    *
    """
    for i in range(val):
        for j in range(val - i, 0, -1):
            print("*", end="")
        print()


def starPattern4(val):
    """
    inverse right align

    *****
     ****
      ***
       **
        *

    """
    for i in range(val):
        for j in range(i):
            print(" ", end="")
        for k in range(val - i):
            print("*", end="")
        print()


def starPattern5(val):
    """
    pyramid

        *
       * *
      * * *
     * * * *
    * * * * *

    """
    for i in range(val):
        for j in range(val - i - 1):
            print(" ", end="")
        for k in range(i + 1):
            print("* ", end="")
        print()


def starPattern6(val):
    """
    inverse pyramid

    * * * * *
     * * * *
      * * *
       * *
        *

    """
    for i in range(val):
        for j in range(i):
            print(" ", end="")
        for k in range(val - i):
            print("* ", end="")
        print()


def starPattern7(val):
    """
    diamond

       *
      * *
     * * *
    * * * *
     * * *
      * *
       *

    """
    for i in range(val * 2):
        if i // val == 0:
            print("+1")
        else:
            print("-1")


starPattern7(val)
