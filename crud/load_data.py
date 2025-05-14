import json
from models.models import Author, Quote
from config.connect_db import conn


def insert_authors():
    with open('json/authors.json', encoding='utf-8') as f:
        authors = json.load(f)
        for a in authors:
            author = Author(**a)
            author.save()


def insert_quotes():
    with open('json/quotes.json', encoding='utf-8') as f:
        quotes = json.load(f)
        for q in quotes:
            author = Author.objects(fullname=q['author']).first()
            if author:
                quote = Quote(tags=q['tags'], author=author, quote=q['quote'])
                quote.save()
