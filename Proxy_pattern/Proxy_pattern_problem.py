from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)
from abc import abstractmethod
from time import sleep

"""The Proxy pattern looks like the thing it is proxy-ing for. 
The Head First Into Desing Patterns book splits this pattern into three categories.
Remote proxy: Should be used when accessing something "remote".
(a resource on another server, something from a different code project, etc.)

Virtual proxy: Controls access toa  resource that is expensive to create.
(similar to lazy evaluation, this proxy makes sure you actually interact with the expensive resource if you really really need to.)

Protection proxy: Controls access to a resource based on access rights.
(Manages access to a resource when not just any user should have access to it.)

The following is an example of where a Virtual Proxy would be useful. See the other script in this directory for the implementation.
"""

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
        sleep(3)
        self.numberOfPages = 0
        self.numberOfChapters = 0
        self.numberOfAdverbs = 0

    def numberOfPages(self):
        return self.numberOfPages
    def numberOfChapters(self):
        return self.numberOfChapters
    def numberOfAdverbs(self):
        return self.numberOfAdverbs

def main():
    """We assume that for some reason, in our application, we instantiate book parsers
    even though we never access the results of the parsing. We also do not wish to change this behavior."""
    book = "..."

    parser = BookParser(book)
    """It's easy to see how this might quickly become an issue with a few more books and instantiations of the parser."""
    

if __name__ == '__main__':
    main()