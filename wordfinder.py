from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file):
        """creates a variable file from the argument passed in"""
        self.file = file
        self.words = open(f'{self.file}', 'r')
        self.length = len(self.words.readlines())
        print(f"{self.length} words read")

    def random(self):
        pass

