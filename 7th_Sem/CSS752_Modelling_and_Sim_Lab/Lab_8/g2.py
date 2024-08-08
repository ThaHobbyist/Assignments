import random
import numpy as np

# Define the utility matrix for Player A
utility_matrix_A = np.array([
    [0, -1, 1],  # Player A chooses Rock
    [1, 0, -1],  # Player A chooses Paper
    [-1, 1, 0]   # Player A chooses Scissors
])

# Define the utility matrix for Player B
utility_matrix_B = -utility_matrix_A  # Symmetrically opposite to Player A

def play_rps_game(p_A, p_B):
    # Randomly choose Player B's strategy based on probabilities
    choice_B = np.random.choice(['Rock', 'Paper', 'Scissors'], p=p_B)

    # Calculate Player A's expected utilities for each choice
    expected_utilities_A = np.dot(p_A, utility_matrix_A)

    # Find Player A's best response to Player B's choice
    best_response_A = np.argmax(expected_utilities_A)

    # Translate the best response into Player A's choice
    choices_A = ['Rock', 'Paper', 'Scissors']
    choice_A = choices_A[best_response_A]

    # Calculate Player A's utility in this round
    utility_A = utility_matrix_A[best_response_A, choices_A.index(choice_B)]

    return choice_A, choice_B, utility_A

def simulate_rps_game(n):
    # Initialize counters for the number of times each choice is made
    choice_counts_A = {'Rock': 0, 'Paper': 0, 'Scissors': 0}
    choice_counts_B = {'Rock': 0, 'Paper': 0, 'Scissors': 0}

    total_utility_A = 0

    for _ in range(n):
        # Generate random probabilities for Player A and Player B
        p_A = np.random.dirichlet(np.ones(3))
        p_B = np.random.dirichlet(np.ones(3))

        choice_A, choice_B, utility_A = play_rps_game(p_A, p_B)

        # Update choice counts
        choice_counts_A[choice_A] += 1
        choice_counts_B[choice_B] += 1

        total_utility_A += utility_A

    return choice_counts_A, choice_counts_B, total_utility_A / n

# Number of iterations for the simulation
n = int(input("Enter the number of iterations: "))

choice_counts_A, choice_counts_B, avg_utility_A = simulate_rps_game(n)

print(f"Player A's choices: {choice_counts_A}")
print(f"Player B's choices: {choice_counts_B}")
print(f"Average utility for Player A: {avg_utility_A}")
print(f"Average utility for Player B: {avg_utility_A}")
