# Define the original grammar
grammar = {
    'S': ["S+T", "aA"],
    'A': ["Ab", "cB"],
    'B': ["d"],
    'T': ["e"]
}

# Define the new grammar
new_grammar = {}

# Step 1: Create a new non-terminal for each left-recursive production
for symbol in grammar:
    new_productions = []
    new_symbol = symbol + "`"
    for production in grammar[symbol]:
        if production[0] == symbol:
            new_productions.append(production[1:] + new_symbol)
        else:
            new_productions.append(production + new_symbol)
    new_grammar[symbol] = new_productions
    new_grammar[new_symbol] = [production for production in grammar[symbol] if production[0] == symbol] + ['']

# Step 2: Add productions for the new non-terminals
for symbol in grammar:
    for production in grammar[symbol]:
        if production[0] == symbol:
            new_symbol = symbol + "`"
            new_productions = [production[1:] + new_symbol for production in grammar[symbol]]
            new_grammar[new_symbol].extend(new_productions)
        else:
            new_grammar[symbol].append(production)

# Print the new grammar
print("Original Grammar:\n", grammar)
print("New Grammar:\n", new_grammar)
