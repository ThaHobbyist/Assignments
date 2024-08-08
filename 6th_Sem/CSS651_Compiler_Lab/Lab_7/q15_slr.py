from collections import defaultdict

# define the grammar productions
productions = {
    'S': ['A'],
    'A': ['Ab', 'a'],
}

# define the follow sets
follow_sets = {
    'S': ['$'],
    'A': ['b', '$'],
}

# define the first sets
first_sets = {
    'S': ['a'],
    'A': ['a', 'b'],
}

# define the LR(0) items
lr0_items = {
    'S': [('S', 0)],
    'A': [('A', 0), ('A', 1)],
}

# compute the SLR(1) parsing table
parsing_table = defaultdict(dict)

for state, items in lr0_items.items():
    for item in items:
        if item[1] == len(productions[item[0]][item[1]]):
            # reduce action
            for symbol in follow_sets[item[0]]:
                parsing_table[state][symbol] = ('reduce', item[0] + ' -> ' + productions[item[0]][item[1]])
        else:
            # shift or goto action
            symbol = productions[item[0]][item[1]][0]
            if symbol in first_sets.keys():
                # goto action
                goto_state = productions[item[0]][item[1]][0]
                parsing_table[state][symbol] = ('goto', goto_state)
            else:
                # shift action
                shift_state = state + 1
                parsing_table[state][symbol] = ('shift', shift_state)

# print the parsing table
print('SLR(1) Parsing Table:\n')
print('{:<10}{:<10}{:<10}{:<10}'.format('', 'a', 'b', '$'))
for state, actions in parsing_table.items():
    print('{:<10}'.format(state), end='')
    for symbol in ['a', 'b', '$']:
        if symbol in actions.keys():
            action, value = actions[symbol]
            print('{:<10}{:<10}'.format(action + ' ' + str(value), ''), end='')
        else:
            print('{:<10}'.format(''), end='')
    print()
