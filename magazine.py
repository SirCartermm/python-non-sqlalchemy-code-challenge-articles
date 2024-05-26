
from article import Article
from author import Author


class Magazine:
    def __init__(self, name: str, category: str):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be a string with 2-16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string")
        self.name = name
        self.category = category
        self.articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Magazine name must be a string with 2-16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value: str):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Magazine category must be a non-empty string")
        self._category = value

    def add_article(self, article: 'Article'):
        self.articles.append(article)

    def article_titles(self) -> list[str]:
        return [article.title for article in self.articles]

    def contributing_authors(self) -> list[Author]:
        authors = set()
        for article in self.articles:
            authors.add(article.author)
        return list(authors)

    @classmethod
    def top_publisher(cls) -> 'Magazine':
        magazines = "[magazine for magazine in.magazines]"
        if not magazines:
            return None
        return max(magazines, key=lambda m: len(m.articles))