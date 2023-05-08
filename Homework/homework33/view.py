def add_title(title):
    def wrapper(funk):
        def wrap(*args, **kwargs):
            print(f'{title} '.center(50, '='))
            output = funk(*args, **kwargs)
            print('=' * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    def wait_user_answer(self):
        print('Ввод пользовательских данных'.center(50, '='))
        print('Действия с фильмами:')
        print('1 - добавление фильма\n'
              '2 - каталог фильмов\n'
              '3 - просмотр определенного фильма\n'
              '4 - удаление фильма\n'
              'q - выход из программы\n')
        user_answer = input('Выберите вариант действия: ')
        print('=' * 50)
        return user_answer

    @add_title('Редактирование данных каталога фильма')
    def add_user_film(self):
        dict_film = {
            'название': None,
            'жанр': None,
            'режиссер': None,
            'год выпуска': None,
            'длительность': None,
            'студия': None,
            'актеры': None,
        }
        for key in dict_film:
            dict_film[key] = input(f'Введите {key} фильма: ')
        # print('=' * 50)
        return dict_film

    @add_title('Каталог фильмов')
    def show_all_films(self, films):
        for ind, film in enumerate(films, 1):
            print(f'{ind}. {film}')

    @add_title('Просмотр определенного фильма')
    def get_user_film(self):
        user_film = input('Введите название фильма: ')
        return user_film
    @add_title('Просмотр определенного фильма')
    def show_single_film(self, film):
        for key in film:
            print(f'{key} фильма = {film[key]}')
    @add_title('Сообщение об ошибке')
    def show_inkorrect_name_error(self, user_name):
        print(f'Фильма с названием {user_name} не существует')

    @add_title('Удаление определенного фильма')
    def remove_singl_film(self, film):
        print(f'Фильм {film} - был удален')

    @add_title('Сообщение об ошибке')
    def show_inkorrect_answer_error(self, answer):
        print(f'Варианта {answer} не существует')