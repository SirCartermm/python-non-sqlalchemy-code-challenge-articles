def init(self, name): self.name = name self.articles = []

def get_name(self): return self.name

def add_article(self, article): self.articles.append(article)

def get_articles(self): return self.articles

def get_magazines(self): magazines = set() for article in self.articles: magazines.add(article.magazine) return list(magazines)

def get_topic_areas(self): topics = set() for article in self.articles: topics.add(article.topic) return list(topics)