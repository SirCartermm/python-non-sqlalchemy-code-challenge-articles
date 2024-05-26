from article import Article
from magazine import Magazine


class Author:
    def __init__(self, name: str):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string")
        self.name = name
        self.articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Author name must be a non-empty string")
        self._name = value

    def add_article(self, article: 'Article'):
        self.articles.append(article)

    def articles_written(self) -> list['Article']:
        return self.articles

    def magazines_contributed_to(self) -> list['Magazine']:
        magazines = set()
        for article in self.articles:
            magazines.add(article.magazine)
        return list(magazines)

    def topic_areas(self) -> list[str]:
        categories = set()
        for article in self.articles:
            categories.add(article.magazine.category)
        return list(categories)

