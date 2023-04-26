from parsers import Parser


def main():
    pars = Parser('https://omsk.nix.ru/price.html?section='
                  'notebooks_all#c_id=256&fn=256&g_id=327&manual_fts_fn='
                  '0&page=1&sort=%2Bp8116%2B8120%2B8119%2B330%2B90&spoiler='
                  '&store=msk-0_1072_1&thumbnail_view=2', 'kit.txt')
    # pars.run
    pars.get_html()
    pars.parsing()


if __name__ == '__main__':
    main()
