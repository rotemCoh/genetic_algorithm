import random
class Person:

    def __init__(self, code, fitness, alphabet):
        self.code = code
        self.fitness = fitness
        self.alphabet = alphabet
        self.new_code = self.update_code()

    def update_code(self):
        updated_code = ""
        for char in self.code:
            if char.isalpha():
                updated_code += self.alphabet[char.upper()]
            else:
                updated_code += char
        return updated_code

    def mutate(self):
        # Select a random position in the code
        print(self.new_code)
        print(self.alphabet)
        # Filter out non-letter characters
        letters = [char for char in self.code if char.isalpha()]

        # Randomly choose a letter to replace
        if letters:
            letter_to_replace = (random.choice(letters)).upper()
            print("letter_to_replace: " +str(letter_to_replace) + "\n")

        # Randomly choose a replacement letter
        replacement_letter = random.choice(list(self.alphabet.keys()))

        # update the dictionary
        self.alphabet[letter_to_replace], self.alphabet[replacement_letter] = self.alphabet[replacement_letter], self.alphabet[letter_to_replace]
        self.new_code = self.update_code()

    def get_code(self):
        return self.code

    def get_new_code(self):
        return self.new_code

    def get_fitnees(self):
        return self.fitness
    def get_alphabet(self):
        return self.alphabet
