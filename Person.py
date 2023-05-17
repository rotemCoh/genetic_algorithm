import random
import string
class Person:
    def __init__(self, code,fitness):
        self.code = code
        self.alphabet = {}
        self.alphabet = self.generate_random_alphabet()
        self.update_code()
        self.fitness = fitness

    def update_code(self):
        updated_code = ""
        for char in self.code:
            if char.isalpha():
                updated_code += self.alphabet[char.upper()]
            else:
                updated_code += char
        self.code = updated_code
        
    def generate_random_alphabet(self):
        alphabet = {'A': 't', 'B': 'g', 'C': 'o', 'D': 'n', 'E': 'b', 'F': 'h', 'G': 'i', 'H': 'v', 'I': 'j', 'J': 'z', 'K': 'k', 'L': 'y', 'M': 'w', 'N': 'm', 'O': 'x', 'P': 'd', 'Q': 'q', 'R': 'p', 'S': 'c', 'T': 'a', 'U': 'r',
        'V': 'e', 'W': 's', 'X': 'u', 'Y': 'f', 'Z': 'l'}
        random_alphabet = {}
        available_letters = list('abcdefghijklmnopqrstuvwxyz')
        for key in alphabet:
            random_index = random.randint(0, len(available_letters) - 1)
            random_letter = available_letters.pop(random_index)
            random_alphabet[key] = random_letter
        return random_alphabet

    def get_code(self):
        return self.code
    def get_fitnees(self):
        return self.fitness



