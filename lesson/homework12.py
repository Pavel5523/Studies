# s = 0


# def paral(a, b, c):
#     s1 = 0
#     s2 = 0
#     s3 = 0
#
#     def sqr():
#         nonlocal s1, s2, s3
#         s1 = a * b
#         s2 = a * c
#         s3 = c * b
#
#     sqr()
#     s = 2 * (s1 + s2 + s3)
#     print(s)
#
#
# paral(2, 4, 6)

# def paral(a, b, c):
#     def sqr():
#         global s1, s2, s3
#         s1 = a * b
#         s2 = a * c
#         s3 = c * b
#
#     sqr()
#     s = 2 * (s1 + s2 + s3)
#     print(s)
#
#
# paral(2, 4, 6)


def paral(a, b, c):
    def sqr():
        global s1, s2, s3
        nonlocal s
        s1 = a * b
        s2 = a * c
        s3 = c * b
        s = 0

    sqr()
    s = 2 * (s1 + s2 + s3)
    print(s)


paral(2, 4, 6)
