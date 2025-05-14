from crud import load_data as load
from models.models import Author, Quote
from config.connect_db import conn


def search_by_author(name):
    author = Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        for quote in quotes:
            print(quote.quote.encode('utf-8').decode())


def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    for quote in quotes:
        print(quote.quote.encode('utf-8').decode())


def search_by_tags(tags):
    tag_list = tags.split(',')
    quotes = Quote.objects(tags__in=tag_list)
    for quote in quotes:
        print(quote.quote.encode('utf-8').decode())


def main():
    load.insert_authors()
    load.insert_quotes()

    while True:
        command = input("Введіть команду (name/tag/tags/exit): ")
        if command.startswith("name:"):
            name = command.split(":", 1)[1].strip()
            search_by_author(name)
        elif command.startswith("tag:"):
            tag = command.split(":", 1)[1].strip()
            search_by_tag(tag)
        elif command.startswith("tags:"):
            tags = command.split(":", 1)[1].strip()
            search_by_tags(tags)
        elif command == "exit":
            break
        else:
            print("Невідома команда")


if __name__ == "__main__":
    main()
