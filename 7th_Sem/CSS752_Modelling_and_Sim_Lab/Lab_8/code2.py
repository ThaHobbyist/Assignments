import random

print("Sayantani Karmakar, 20CS8024 \n")
# Initialize the payoff matrices
payoff_matrix_a = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
payoff_matrix_b = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]

# Initialize the mixed strategies for both players (e.g., random initial strategies)
p_R = random.random()
p_P = random.random()
p_S = 1 - p_R - p_P

q_R = random.random()
q_P = random.random()
q_S = 1 - q_R - q_P

# Number of iterations for the simulation
num_iterations = int(input("Enter the number of iterations: "))

# Initialize cumulative payoffs
cumulative_payoff_a = 0
cumulative_payoff_b = 0

# Simulation loop
for _ in range(num_iterations):
    # Randomly choose actions based on mixed strategies
    action_a = random.choices(
        ['Rock', 'Paper', 'Scissors'], weights=[p_R, p_P, p_S])[0]
    action_b = random.choices(
        ['Rock', 'Paper', 'Scissors'], weights=[q_R, q_P, q_S])[0]

    # Sayantani Karmakar, 20CS8024
    # Update cumulative payoffs
    cumulative_payoff_a += payoff_matrix_a[['Rock', 'Paper', 'Scissors'].index(
        action_a)][['Rock', 'Paper', 'Scissors'].index(action_b)]
    cumulative_payoff_b += payoff_matrix_b[['Rock', 'Paper', 'Scissors'].index(
        action_b)][['Rock', 'Paper', 'Scissors'].index(action_a)]

# Calculate average payoffs
average_payoff_a = cumulative_payoff_a / num_iterations
average_payoff_b = cumulative_payoff_b / num_iterations

print("Average Payoff for Player A:", average_payoff_a)
print("Average Payoff for Player B:", average_payoff_b)
