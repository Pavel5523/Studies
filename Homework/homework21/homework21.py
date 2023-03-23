class Formulas:

    @staticmethod
    def maximum(*args):
        return max(args)

    @staticmethod
    def minimum(*args):
        return min(args)

    @staticmethod
    def average(*args):
        return sum(args) / len(args)

    @staticmethod
    def factorial(a):
        f = 1
        for i in range(1, a + 1):
            f *= i
        return f


print('Минимальное число:', Formulas.minimum(3, 5, 7, 9))
print('Максимальное число:', Formulas.maximum(3, 5, 7, 9))
print('Среднее арифметическое:', Formulas.average(3, 5, 7, 9))
print('Факториал числа:', Formulas.factorial(5))
