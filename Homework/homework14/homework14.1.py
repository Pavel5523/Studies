try:
    n = [int(input('Введите любое число: ')) for i in range(int(input('Введите количество чисел: ')))]
    print('Введенные числа', n)
    s = 0


    def conclusion(*a):
        for i in a:
            return str(i)


    def search_sum(func):
        def mean_ariphmet():
            global s
            s = sum(n)
            func()

        return mean_ariphmet


    @search_sum
    def s_sum():
        print('Сумма чисел ', conclusion(n), '=', s)
        print('Среднее арифметическое ', n, '=', s / len(n))


    test = search_sum(s_sum)
    test()
except (ZeroDivisionError, ValueError):
    print('Вы ввели не число, либо ноль количества чисел')
