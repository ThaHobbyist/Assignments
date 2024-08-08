grammar = [
    "S -> aB|bC|cD",
    "B -> d|&",
    "C -> e|&",
    "D -> f"
] # Using & as a substitute for EPSILON

def generate_first_sets(grammar):
    first_sets = {}
    for production in grammar:
        lhs, rhs = production.split(' -> ')
        if lhs not in first_sets:
            first_sets[lhs] = set()
        if rhs[0].islower() or rhs[0] == '&':
            first_sets[lhs].add(rhs[0])
        else:
            for symbol in rhs:
                if symbol in first_sets:
                    first_sets[lhs].update(first_sets[symbol])
                    if '&' not in first_sets[symbol]:
                        break
                else:
                    break
    return first_sets

def generate_follow_sets(grammar, first_sets):
    follow_sets = {}
    productions = []
    for production in grammar:
        lhs, rhs = production.split(' -> ')
        productions.append(rhs)
        if lhs not in follow_sets:
            follow_sets[lhs] = set()

    for rhs in productions:
        for i, symbol in enumerate(rhs):
            if symbol.isupper():
                if i == len(rhs) - 1 or rhs[i+1].islower():
                    follow_sets[symbol].add('$')
                for j in range(i+1, len(rhs)):
                    if rhs[j].islower():
                        follow_sets[symbol].add(rhs[j])
                        break
                    elif rhs[j] in first_sets:
                        follow_sets[symbol].update(first_sets[rhs[j]])
                        if '&' not in first_sets[rhs[j]]:
                            break
                    else:
                        break
    return follow_sets

first = generate_first_sets(grammar)
follow = generate_follow_sets(grammar, first)
print("First: ", first)
print("Follow: ", follow)