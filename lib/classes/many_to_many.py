class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []

    def __str__(self):
        return self.name

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles = []

    def __str__(self):
        return self.name

class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")

        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        author.articles.append(self)
        magazine.articles.append(self)

    def __str__(self):
        return self.title