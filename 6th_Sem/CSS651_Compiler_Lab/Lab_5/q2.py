from q1 import grammar, generate_first_sets, generate_follow_sets
first_sets = generate_first_sets(grammar)
follow_sets = generate_follow_sets(grammar, first_sets)
# Grammar uses & as symbol for EPSILON

def print_predictive_parsing_table(grammar, first_sets, follow_sets):
    # Initialize an empty parsing table
    parsing_table = {}

    # Iterate over each production in the grammar
    for production in grammar:
        lhs, rhs = production.split(' -> ')

        
        # Iterate over each terminal in the FIRST set of the production
        for terminal in first_sets[lhs]:
            # Add a SHIFT action to the parsing table
            if lhs not in parsing_table:
                parsing_table[lhs] = {}
            if terminal not in parsing_table[lhs]:
                parsing_table[lhs][terminal] = "SHIFT " + rhs

        # If the FIRST set of the production contains &, add a FOLLOW set action
        if '&' in first_sets[lhs]:
            for terminal in follow_sets[lhs]:
                if lhs not in parsing_table:
                    parsing_table[lhs] = {}
                if terminal not in parsing_table[lhs]:
                    parsing_table[lhs][terminal] = "FOLLOW " + lhs

        # If the FIRST set of the production doesn't contain &, add a REDUCE action
        else:
            for terminal in first_sets[lhs]:
                if lhs not in parsing_table:
                    parsing_table[lhs] = {}
                if terminal not in parsing_table[lhs]:
                    parsing_table[lhs][terminal] = "REDUCE " + production

    # Print the parsing table
    for nonterminal, actions in parsing_table.items():
        print(f"{nonterminal}:")
        for terminal, action in actions.items():
            print(f"\t{terminal}: {action}")

print_predictive_parsing_table(grammar, first_sets, follow_sets)

