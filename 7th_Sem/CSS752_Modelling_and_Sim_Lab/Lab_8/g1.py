import random

def play_prisoners_dilemma(payoff_matrix):
    
    # Decide the strategy for each player 
    expected_payoffs = {
        'Cooperate': 0.5 * payoff_matrix[('Cooperate', 'Cooperate')][0] + 0.5 * payoff_matrix[('Cooperate', 'Defect')][0],
        'Defect': 0.5 * payoff_matrix[('Defect', 'Cooperate')][0] + 0.5 * payoff_matrix[('Defect', 'Defect')][0],
    }

    if expected_payoffs['Cooperate'] > expected_payoffs['Defect']:
        player1_strategy = 'Cooperate'
    else:
        player1_strategy = 'Defect'

    if expected_payoffs['Cooperate'] > expected_payoffs['Defect']:
        player2_strategy = 'Cooperate'
    else:
        player2_strategy = 'Defect'

    player1_payoff, player2_payoff = payoff_matrix[(player1_strategy, player2_strategy)]

    return player1_strategy, player2_strategy, player1_payoff, player2_payoff

def simulate_prisoners_dilemma(n, payoff_matrix):
    player1_total_payoff = 0
    player2_total_payoff = 0

    for _ in range(n):
        player1_strategy, player2_strategy, player1_payoff, player2_payoff = play_prisoners_dilemma(payoff_matrix)
        player1_total_payoff += player1_payoff
        player2_total_payoff += player2_payoff

    avg_player1_payoff = player1_total_payoff / n
    avg_player2_payoff = player2_total_payoff / n

    return avg_player1_payoff, avg_player2_payoff

def get_payoff_matrix():
    # function to get the payoff matrix from user input
    payoff_matrix = {}
    for i in range(2):
        for j in range(2):
            print(f"Enter the payoff for strategy {i+1} and {j+1}")
            payoff_matrix[(i+1, j+1)] = tuple(map(int, input().split()))
    
    return payoff_matrix

if __name__ == '__main__':
    payoff_matrix = get_payoff_matrix()

    n = int(input("Enter the number of iterations: "))

    avg_player1_payoff, avg_player2_payoff = simulate_prisoners_dilemma(n, payoff_matrix)

    print(f"Average payoff for Player 1: {avg_player1_payoff}")
    print(f"Average payoff for Player 2: {avg_player2_payoff}")
