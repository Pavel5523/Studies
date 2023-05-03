from parser_homework32 import Parser


def main():
    pars = Parser('https://omsk.velostrana.ru/velozapchasti/kolesa/', 'laptop.csv')
    pars.run()


if __name__ == '__main__':
    main()
