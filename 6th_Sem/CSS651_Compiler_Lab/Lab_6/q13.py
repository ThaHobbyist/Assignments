# Define the grammar
grammar = {
    'S': ['S+S', 'S*S', 'id'],
}

# Input string
input_string = 'id + id * id'

# Initialize the stack and input buffer
stack = ['$', 'S']
input_buffer = input_string.split(' ') + ['$']

# Define a function to print the current state of the parser
def print_state(action, symbol):
    print(f'{stack}\t{input_buffer}\t{action}\t{symbol}')

# Perform the parsing
while True:
    # Print the current state of the parser
    print_state('', '')

    # Get the top symbol of the stack and the first symbol of the input buffer
    top_symbol = stack[-1]
    first_symbol = input_buffer[0]
    print(top_symbol, first_symbol)

    # Check for the shift-reduce conflict
    if top_symbol == 'S' and (first_symbol == '+' or first_symbol == '*'):
        print_state('SHIFT', first_symbol)
        stack.append(first_symbol)
        input_buffer.pop(0)
    elif top_symbol == 'id':
        print_state('REDUCE', top_symbol)
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append('S')
    elif first_symbol == 'id':
        print_state('REDUCE', first_symbol)
        stack.append(first_symbol)
        input_buffer.pop(0)
    elif top_symbol == '$' and first_symbol == '$':
        print_state('ACCEPT', '')
        break
    else:
        print_state('ERROR', '')
        break
