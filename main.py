from Person import Person
from Population import Population
import random
def main():


     given_code = "good djjdjdjdjdjdjdj; djfjfjffjfj. fjjfjfjf,"
     dictionary_file = "dict.txt"

     test = Population(given_code, 1)
     test.generate_random_population()
     test.fitness()
    # flag_for_generation = 0
    # #for i in test.people:
    #  #  print(i.get_new_code())
    # best_string = ""
    # temp_string = ""
    # best_dict = {}
    # temp_dict = {}


    # while(flag_for_generation < 11):
    #     if test.generations == 0:
    #         test.fitness()
    #         best_string, best_dict = test.new_generation()
    #         temp_string = best_string
    #     else:
    #         test.fitness()
    #         temp_string, temp_dict = test.new_generation()
    #     if best_string == temp_string:
    #         flag_for_generation = flag_for_generation + 1
    #         best_dict = temp_dict
    #     else:
    #         best_string = temp_string
    # print(best_dict)
    # Open a file in write mode
    # with open("plain.txt", "w") as file:
    #     # Write the string to the file
    #     file.write(best_string)
    #
    # # Open a file in write mode
    # with open("perm.txt", "w") as file:
    #     # Iterate over dictionary items and write them to the file
    #     for key, value in best_dict.items():
    #         file.write(key.lower() + " " + value + "\n")

    #return best_string
    # print(best_string)
    # print(test.generations)
    #for q in test.people:
     #  print("new :" + str(i.get_new_code()))
    # for p in test.people:
    #     # print(p.get_fitness())
    #     p.mutate()

    # taco = test.get_people()
    # for t in taco:
    #     print(t.get_code())

    #selected_people = random.sample(test.get_people(), 2)


if __name__ == "__main__":
    main()