
from author import Author
from magazine import Magazine


class Article:
    def __init__(self, author: Author, magazine: Magazine, title: str):
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Article title must be a string with 5-50 characters")
        self.author = author
        self.magazine = magazine
        self.title = title
        author.add_article(self)
        magazine.add_article(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Article title must be a string with 5-50 characters")
        self._title = value


# Example usage:
author1 = Author("John Doe")
author2 = Author("Jane Smith")
magazine1 = Magazine("Tech News", "Technology")
magazine2 = Magazine("Health Journal", "Health")

article1 = Article(author1, magazine1, "AI in Healthcare")
article2 = Article(author2, magazine1, "Robotics in Surgery")
article3 = Article(author1, magazine2, "Nutrition and Wellness")

print(magazine1.article_titles())  # Output: ["AI in Healthcare", "Robotics in Surgery"]
print(author1.topic_areas())  # Output: ["Technology", "Health"]
print(Magazine.top_publisher().name)  # Output: "Tech News"