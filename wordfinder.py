from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """creates a variable file from the argument passed in"""
        file = open(path)
        self.words = self.taco(file)
        print('self.words',self.words)
        # self.text = open(self.file)
        # self.words_list = self.text.readlines()
        # print("self.words_list", self.words_list)
        # self.new_list = self.taco()
        # print("self.new_list", self.new_list)
        self.length = len(self.words)
        print(f"{self.length} words read")

    def __repr__(self):
        return f'<WordFinder file = {self.file}>'

    def random(self):
        """returns random word from list"""
        return choice(self.new_list)

    def taco(self, file):
        print('parse is being called!')
        return [word.strip() for word in file]

class SpecialWordFinder(WordFinder):
    """ Special Word Find: finds random words in text file that
    spaces and # symbols"""

    def taco(self, file):
      return [word for word in super().taco(file) if not word.startswith("#") and word != ""]
