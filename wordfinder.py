from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file):
        """creates a variable file from the argument passed in"""
        self.file = file
        self.words = open(f'{self.file}', 'r')
        self.words_list = self.words.readlines()
        self.new_list = [word.strip() for word in self.words_list]
        self.length = len(self.new_list)
        print(f"{self.length} words read")

        #new_list = [item.strip() for item in my_list]

    def random(self):
        return choice(self.new_list)


class SpecialWordFinder(WordFinder):
