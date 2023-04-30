from parser_homework32 import Parser


def main():
    pars = Parser('https://radec-m.ru/radiodetali/13772/', 'laptop.csv')
    pars.run()


if __name__ == '__main__':
    main()
