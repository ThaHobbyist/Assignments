# Define the grammar
grammar = {
    'S': ['bCEi'],
    'C': ['dD'],
    'D': ['cD', '&'],
    'E': ['FG'],
    'F': ['h', '&'],
    'G': ['g']
}


# Define the recursive descent parser with added print statements
def parse_S(tokens):
    print(f'Parsing S: {tokens}')
    if tokens[0] == 'b':
        if tokens[1] == 'd':
            parse_C(tokens[1:])
            if tokens[-1] == 'i':
                return
            else:
                raise Exception('Invalid input')
        else:
            raise Exception('Invalid input')
    else:
        raise Exception('Invalid input')

def parse_C(tokens):
    print(f'Parsing C: {tokens}')
    if tokens[0] == 'd':
        parse_D(tokens[1:])
    elif tokens[0] == 'h':
        parse_E(tokens)
        return
    else:
        return

def parse_D(tokens):
    print(f'Parsing D: {tokens}')
    if tokens[0] == 'c':
        parse_D(tokens[1:])
    elif tokens[0] == 'h':
        parse_E(tokens)
        return
    else:
        return

def parse_E(tokens):
    print(f'Parsing E: {tokens}')
    parse_F(tokens[0:])
    parse_G(tokens[1:])

def parse_F(tokens):
    print(f'Parsing F: {tokens}')
    if tokens[0] == 'h':
        return
    elif tokens[0] == '&':
        return
    else:
        return

def parse_G(tokens):
    print(f'Parsing G: {tokens}')
    if tokens[0] == 'g':
        return
    elif tokens[0] == '&':
        return
    else:
        return

# Define the input string
input_string = 'bdcchi'

# Parse the input string
parse_S(input_string)

# Print success message
print('Parsing successful!')
