import random
import math


def map(i):
    result = 0
    for pos in swap:
        result = (result << 1) | (((1 << pos) & i) >> pos)
    return result ^ invert


def unmap(i):
    i = i ^ invert
    result = 0
    for pos in unswap:
        result = (result << 1) | (((1 << pos) & i) >> pos)
    return result


if __name__ == '__main__':
    bits = 16

    swap = [x for x in range(bits)]
    unswap = [x for x in range(bits)]

    invert = random.getrandbits(bits)

    random.shuffle(swap)

    print(swap)

    for i, x in enumerate(swap):
        # print(x, bits - i - 1)
        unswap[bits - x - 1] = bits - i - 1

    test_a = []
    test_b = []
    for i in range(10):
        i = random.getrandbits(bits)
        c = map(i)
        u = unmap(c)
        print (i,c,u)
        test_a.append(c)
        test_b.append(i)

    print(len(list(set(test_a))) == len(test_b))
