from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)
from abc import abstractmethod
from time import sleep



class IBookParser(ABC):
    @abstractmethod
    def parse(self):
        pass
    @abstractmethod
    def numberOfPages(self):
        pass
    @abstractmethod
    def numberOfChapters(self):
        pass
    @abstractmethod
    def numberOfAdverbs(self):
        pass

class BookParser(IBookParser):
    def __init__(self, book):
        """The book parser parses a book when it is instantiated."""
        self.book = book
        self.parse()

    def parse(self):
        """Heavy computational work."""
        sleep(5)
        self.numberOfPages = 0
        self.numberOfChapters = 0
        self.numberOfAdverbs = 0

    def numberOfPages(self):
        return self.numberOfPages
    def numberOfChapters(self):
        return self.numberOfChapters
    def numberOfAdverbs(self):
        return self.numberOfAdverbs

class LazyBookParserProxy(IBookParser):
    def __init__(self, book):
        self.book = book
        self.real_book_parser = None
    
    def parse(self):
        self.real_book_parser = BookParser(self.book)
    
    def numberOfPages(self):
        if self.real_book_parser is None:
            self.parse()
        return self.real_book_parser.numberOfPages

    def numberOfChapters(self):
        if self.real_book_parser is None:
            self.parse()
        return self.real_book_parser.numberOfChapters

    def numberOfAdverbs(self):
        if self.real_book_parser is None:
            self.parse()
        return self.real_book_parser.numberOfAdverbs



def main():
    """We assume that for some reason, in our application, we instantiate book parsers
    even though we never access the results of the parsing. We also do not wish to change this behavior."""
    book1, book2, book3 = "...", "...", "..."

    parser1, parser2, parser3 = LazyBookParserProxy(book1), LazyBookParserProxy(book2), LazyBookParserProxy(book3)

    print(parser3.numberOfPages()) #only book3 gets an actual BookParser instantiated
    

if __name__ == '__main__':
    main()