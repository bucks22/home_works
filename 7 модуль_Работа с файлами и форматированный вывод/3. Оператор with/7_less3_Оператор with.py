

import string
from collections import Counter


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = {}

    def get_all_words(self):
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                translator = str.maketrans('', '', string.punctuation)
                content = content.translate(translator)
                words = content.lower().split()
                self.all_words[file_name] = words
        return self.all_words

    def find(self, word):
        all_words = self.get_all_words()
        self.find_word = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                index = words.index(word) + 1
                self.find_word[name] = index
            else:
                print(f'Слово {word} не найдено в словаре {name}')
        return self.find_word

    def count(self, word):
        self.count_word = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            count = words.count(word)
            self.count_word[name] = count
        return self.count_word


finder2 = WordsFinder('test_file.txt', 'test2.txt')
print(finder2.get_all_words())
print(finder2.find('PoTATO'))
print(finder2.count('text'))
