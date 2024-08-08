import random

print("Sayantani Karmakar, 20CS8024 \n")
# Define the payoffs
payoffs = {
    ('C', 'C'): (3, 3),
    ('D', 'D'): (1, 1),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
}

# Initialize variables
total_payoff_A = 0
total_payoff_B = 0
num_rounds = int(input("Enter the number of rounds: "))

for round in range(num_rounds):
    choice_A = random.choice(['C', 'D'])
    choice_B = random.choice(['C', 'D'])

    # Calculate and display the payoffs for both players
    payoff_A, payoff_B = payoffs[(choice_A, choice_B)]  # type: ignore
    print(
        f"Round {round + 1}: Player A chose {choice_A}, Player B chose {choice_B}")
    print(f"Player A payoff: {payoff_A}, Player B payoff: {payoff_B}")

    # Sayantani Karmakar, 20CS8024
    # Update the total payoff for each player
    total_payoff_A += payoff_A
    total_payoff_B += payoff_B

# Calculate the average payoff for each player
average_payoff_A = total_payoff_A / num_rounds
average_payoff_B = total_payoff_B / num_rounds

# Analyze the results
print("\nResults:")
print(f"Average payoff for Player A: {average_payoff_A}")
print(f"Average payoff for Player B: {average_payoff_B}")

# Determine if there is a dominant strategy
if average_payoff_A > average_payoff_B:
    dominant_strategy = 'A'
elif average_payoff_B > average_payoff_A:
    dominant_strategy = 'B'
else:
    dominant_strategy = None

if dominant_strategy:
    print(f"Player {dominant_strategy} has a dominant strategy.")
else:
    print("There is no dominant strategy.")
