"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """
        Finds a random word out of a given text file
    """
    
    def __init__(self, text):
        self.text = text
        file = open(text)
        self.words = self.parse(file)

    def __repr__(self, text):
        return f"<Word Finder File: {self.text}>"

    def parse(self, file):
        """makes file into a list of words"""
        return [words.strip() for words in file]
    
    def random(self):
        """Returns a random word from the file"""
        return random.choice(self.words)
    

class SpecialWordFinder:
    """
    A more specialized word finder that skip over blank or commented lines
    """

    def __init__(self):
        super().__init__(WordFinder)
    
    def parse(self, file):
        """Make a file into a list of words while skipping over blanks and comments"""
        return [words.strip() for words in file if words.strip() and not words.startswith('#')]