from parser_homework32 import Parser

res = 'https://omsk.velostrana.ru/velozapchasti/kolesa/'


def main():
    for i in range(6):
        if i == 0:
            res_new = res
        else:
            res_new = res + str(i + 1) + '.html'
        pars = Parser(res_new, 'Kolesa.csv')
        pars.run()


if __name__ == '__main__':
    main()
