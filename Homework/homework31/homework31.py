from parsers import Parser

def main():
    pars = Parser('https://www.danomsk.ru/shop/769-instrument/774-nabory/', 'kit.txt')
    pars.run

if __name__ == '__main__':
    main()
