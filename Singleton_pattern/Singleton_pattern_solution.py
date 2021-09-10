from __future__ import annotations

"""The Singleton pattern is designed to make it impossible to create more than one instance
of that object."""

class Singleton:
    
    __instance = None #dunder at the beginning of a variable name is a convention in Python to say that the variable should be considered private

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Cannot call constructor, an instance already exists")
        else:
            Singleton.__instance = self

    @staticmethod
    def getInstance() -> Singleton:
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

def main():
    singleton = Singleton()
    print(singleton)
    singleton = Singleton.getInstance()
    print(singleton) #same address in memory as before



if __name__ == '__main__':
    main()