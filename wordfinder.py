"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    def __init__(self, path):
        """ reads path and creates database of words and # of words contained"""
        dict_file = open(path)
        self.path = path
        self.words = self.parse(dict_file)
        # can't use return in init to print
        print (f"{len(self.words)} words read")

    def __repr__(self):
        """returns string containing length and path"""
        return f"Contains {len(self.words)} words from {self.path}"

    def parse(self, dict_file):
        """creates a list containined words in file stripped of spaces"""
        return [w.strip() for w in dict_file]

    def random(self):
        """uses imported random method to choose random word from file """
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    # no need to add below, same as before
    # def __init__(self, path):
    #     # no need to redeclare self, already in super().__init__
    #     super().__init__(path)
    
    def parse(self, dict_file):
        """returns words that are not empty strings and don't start with #"""
        # return [w.strip() for w in dict_file if not(w.startswith('#') and w.startswith(' '))]
        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]
        # strip word and add to list IF it doesn't start with # AND it's truthy
        # w.strip() strips the entry of spaces. empty string returns falsy
        # only w.strip() for w if entry doesn't start with # and is a truthy value

