from SvennMethod import FindUnimodalSegment

func = lambda x: x ** 2 + 1
(a, b) = FindUnimodalSegment(-5, 0.1, func)
print(a)
print(b)