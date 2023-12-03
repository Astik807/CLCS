import random
from deap import base, creator, tools, algorithms

# Define the customer support process
process = {
    "start": "Customer submits a ticket",
    "steps": [
        {
            "name": "Agent reviews ticket",
            "success_rate": 0.8,
            "next_step": "Agent resolves ticket"
        },
        {
            "name": "Agent escalates ticket",
            "success_rate": 0.2,
            "next_step": "Specialist reviews ticket"
        },
        {
            "name": "Specialist reviews ticket",
            "success_rate": 0.9,
            "next_step": "Specialist resolves ticket"
        },
        {
            "name": "Agent closes ticket",
            "success_rate": 1.0,
            "next_step": "None"
        }
    ]
}

# Create the genetic algorithm framework
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Define the genetic algorithm parameters
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=len(process['steps']))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Define the evaluation function
def evaluate(individual):
    total_success_rate = sum(step['success_rate'] * gene for step, gene in zip(process['steps'], individual))
    return total_success_rate,

toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.2, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)

# Create an initial population
population = toolbox.population(n=10)

# Run the genetic algorithm
algorithms.eaMuPlusLambda(population, toolbox, mu=10, lambda_=100, cxpb=0.7, mutpb=0.2, ngen=50, stats=None, halloffame=None)

# Get the best individual
best_individual = tools.selBest(population, k=1)[0]

# Create the optimized process
optimized_process = {
    "start": "Customer submits a ticket",
    "steps": [
        {
            "name": step["name"],
            "success_rate": best_gene,
            "next_step": step["next_step"]
        } for step, best_gene in zip(process['steps'], best_individual)
    ]
}

# Print the optimized process
print(optimized_process)
