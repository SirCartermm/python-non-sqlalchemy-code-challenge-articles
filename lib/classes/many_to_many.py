class Article:
    all = []

    def _init_(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, "title"):
            AttributeError("Title cannot be changed")
        else:
            if isinstance(new_title, str):
                if 5 <= le