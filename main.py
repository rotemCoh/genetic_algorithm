from Person import Person
from Population import Population
from Population_darvin import Population_darvin
import random
def main():
    with open('enc.txt', 'r') as file:
        given_code = file.read().replace('\n', '')
    test = Population_darvin(given_code, 200,3)
    test.generate_random_population()
    flag_for_generation = 0
    best_string = ""
    temp_string = ""
    best_fit = 0
    best_dict = {}
    temp_dict = {}


    while(flag_for_generation < 11):
        if test.generations == 0:
            test.fitness()
            best_string, best_dict, fitness = test.new_generation()
            temp_string = best_string
        else:
            test.fitness()
            temp_string, temp_dict, fitness = test.new_generation()
        if fitness == best_fit:
            flag_for_generation += 1
        else:
            best_string = temp_string
            best_dict = temp_dict
            best_fit = fitness
            flag_for_generation = 0

    print(best_dict)
    with open("plain.txt", "w") as file:
        # Write the string to the file
        file.write(best_string)

    # Open a file in write mode
    with open("perm.txt", "w") as file:
        # Iterate over dictionary items and write them to the file
        for key, value in best_dict.items():
            file.write(key.lower() + " " + value + "\n")

if __name__ == "__main__":
    main()