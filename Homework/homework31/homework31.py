from parsers import Parser


def main():
    pars = Parser('https://omsk.nix.ru/price.html?section=notebooks_all#c_id=256&fn=256&g_id=490&manual_fts_fn='
                  '0&page=all&sort=%2Bp8116%2B8120%2B8119%2B330%2B90&spoiler=&store='
                  'msk-0_1072_1&thumbnail_view=2', 'laptop.csv')
    pars.run()


if __name__ == '__main__':
    main()
