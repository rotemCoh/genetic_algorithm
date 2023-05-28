import matplotlib.pyplot as plt

def plot():
    # Read the file and extract the data
    with open('result1.txt', 'r') as file:
        lines = file.read().splitlines()

    fitness = []
    generation = []

    # Extract fitness and generation data from the file
    for i in range(0, len(lines), 2):
        try:
            fitness.append(float(lines[i]))
            generation.append(int(lines[i+1]))
        except (ValueError, IndexError):
            pass

    #print(fitness)
    #print(generation)

    # Create the graph
    plt.plot(generation, fitness, marker='o')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Fitness Progression')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot()
