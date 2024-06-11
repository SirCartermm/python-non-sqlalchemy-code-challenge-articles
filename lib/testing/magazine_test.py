class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles = []

    def __str__(self):
        return self.name

    def article_titles(self):
        if not self.articles:
            return None
        return [article.title for article in self.articles]

    def contributors(self):
        if not self.articles:
            return []
        return list(set([article.author for article in self.articles]))

    def contributing_authors(self):
        if not self.articles:
            return []
        authors = {}
        for article in self.articles:
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        return [author for author, count in authors.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        max_count = max(len(magazine.articles) for magazine in cls.all)
        top_publishers = [magazine for magazine in cls.all if len(magazine.articles) == max_count]
        return top_publishers[0] if top_publishers else None