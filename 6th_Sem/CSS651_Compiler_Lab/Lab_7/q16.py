class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.rule = None

def postfix_expr(root):
    if root.left is None and root.right is None:
        return root.value
    else:
        left = postfix_expr(root.left)
        right = postfix_expr(root.right)
        return left + " " + right + " " + root.rule

def parse_expr(expr):
    stack = []
    for char in expr:
        if char.isdigit():
            node = Node(char)
            node.rule = ". → '" + char + "'"
            stack.append(node)
        else:
            if len(stack) < 2:
                print("Error: Invalid input expression")
                return None
            right = stack.pop()
            left = stack.pop()
            node = Node(char)
            node.rule = char + " → ."
            node.left = left
            node.right = right
            stack.append(node)
    if len(stack) != 1:
        print("Error: Invalid input expression")
        return None
    return stack[0]

expr = "9-4+1"

root = parse_expr(expr)

if root is not None:
    postfix = postfix_expr(root)

    print("Postfix expression:", postfix)

    def print_tree(node, level=0):
        if node is not None:
            print("  " * level + "+- " + str(node.rule))
            print_tree(node.left, level + 1)
            print_tree(node.right, level + 1)

    print("Annotated parse tree:")
    print_tree(root)
