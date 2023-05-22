from Person import Person
from Population import Population
import random
def main():
    given_code = "xaac, cbz"
    test = Population(given_code, 10)
    test.generate_random_population()
    # for i in test.people:
        # print(i.get_code())
    # test.fitness()
    # for p in test.people:
    #     # print(p.get_fitnees())
    #     p.mutate()

    # taco = test.get_people()
    # for t in taco:
    #     print(t.get_code())

    selected_people = random.sample(test.get_people(), 2)
    print(str(selected_people[0]))
    print(str(selected_people[1]))
    # alphabet1 = [person["alphabet"] for person in selected_people]
    # alphabet2 = [person["alphabet"] for person in selected_people]
    #
    # test.crossover(alphabet1, alphabet2)


if __name__ == "__main__":
    main()