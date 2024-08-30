# your code goes here!

class Anagram:
    def __init__(self, word):
        # Store the sorted version of the word
        self.sorted_word = ''.join(sorted(word))
    
    def match(self, possible_anagrams):
        # Find all matches by comparing sorted versions
        return [anagram for anagram in possible_anagrams if ''.join(sorted(anagram)) == self.sorted_word]
