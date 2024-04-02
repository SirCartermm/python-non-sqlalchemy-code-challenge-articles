def init(self,name):self.name = name self.articles =

def get_name(self):return self.name

def add_article(self,article):
self.articles.append(article)

def get_articles(self):return self.articles

def get_authors(self):authors = set()for article in
self.articles:authors.add(article.author)return
list(authors)

def get_topic_areas(self): topics = set()for article in
self.articles:topics.add(artical.topic)return list(topics)