from itertools import product
from pprint import pprint
from typing import Tuple

class Word:
    START_SEPARATOR = '<'
    END_SEPARATOR = '>'

    word: Tuple

    def __init__(self, word_as_a_list):
        self.word = tuple(word_as_a_list)

    @classmethod
    def parse(cls, s):
        if s[0] != Word.START_SEPARATOR and s[-1] != Word.END_SEPARATOR:
            raise Exception("Invalid string which is not a word")
        return cls(list(map(int, s[1:-1].split(':'))))

    @classmethod
    def from_tuple(cls, t):
        return Word(list(t))

    @classmethod
    def all_possible_words_list(cls, resolution:int, window_length:int):
        alphabet_list = [x for x in range(-resolution, resolution+1) if x != 0]
        return [Word.from_tuple(t) for t in product(alphabet_list, repeat=window_length)]

    def __eq__(self, other):
        return isinstance(other, Word) and self.word == other.word

    def __lt__(self, other):
        return self.word < other.word

    def __hash__(self):
        return hash(self.word)

    def __str__(self):
        return Word.START_SEPARATOR + ":".join(map(str, self.word)) + Word.END_SEPARATOR

    def __repr__(self):
        return "W" + Word.START_SEPARATOR + ":".join(map(str, self.word)) + Word.END_SEPARATOR

if __name__ == "__main__":
    word = Word.parse("<2:-9:17:10000:234>")
    pprint(word)
    print(Word.parse("<2:-9:17:10000:234>") == Word.parse("<2:-9:17:10000:234>"))
    print(Word.parse("<2:-9:17:10000:234>") == Word.parse("<2:-9:17:10000:235>"))
    print(Word.parse("<2:-9:17:10000:234>") == Word.parse("<2:-9:17:234:10000>"))