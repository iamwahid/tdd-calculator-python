def add(*nums):
    res = 0
    for num in nums:
        if not isinstance(num, int):
            raise Exception("Input should integer")
        res += num
    return res


def sub(*nums):
    res = None
    for num in nums:
        if not isinstance(num, int):
            raise Exception("Input should integer")
        if res is None:
            res = num
            continue
        res -= num
    return res