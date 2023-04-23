class Article:
    def __init__(self, title, autor, pages, description):
        self.title = title
        self.autor = autor
        self.pages = pages
        self.description = description

    def __str__(self):
        return f'{self.title} ({self.autor})'


class ArticleModel:
    def __init__(self):
        self.articles = {}

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_article(self):
        return self.articles.values()

    def get_single_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            'название': article.title,
            'автора': article.autor,
            'количество страниц': article.pages,
            'описание': article.description
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)
