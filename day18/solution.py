import sys
import math
path = sys.argv[1] if len(sys.argv) > 1 else 'puzzle.txt'
with open(path) as file:
    data = file.readlines()

data = [eval(x.strip()) for x in data]


class Node:
    def __init__(self, value=None, parent=None, depth=0):
        self.value = value
        self.child1 = None
        self.child2 = None
        self.parent = parent
        self.depth = depth

    def add_children(self, node1, node2):
        self.child1 = node1
        self.child2 = node2

    def get_sibling(self):
        if self.parent is not None:
            if self.parent.child1 == self:
                return self.parent.child2
            else:
                return self.parent.child1
        return None

    def is_leaf(self):
        return self.child1 is None and self.child2 is None

    def update_value(self, value):
        self.value = value
        if self.parent is None:
            return
        self.parent.update_value(create_list_from_tree(self.parent))


def create_tree(parent, kids):
    if isinstance(kids, list):
        node1 = Node(kids[0], parent, parent.depth+1)
        node2 = Node(kids[1], parent, parent.depth+1)
        create_tree(node1, kids[0])
        create_tree(node2, kids[1])
        parent.add_children(node1, node2)
        return
    else:
        return


def traverse_tree(node, order):
    if isinstance(node, Node):
        traverse_tree(node.child1, order)
        if node.is_leaf():
            order.append(node)
        traverse_tree(node.child2, order)


def has_split(node):
    if isinstance(node, Node):
        if node.is_leaf() and node.value > 9:
            return node
        return has_split(node.child1) or has_split(node.child2)
    return False


def explode_node(node, order, depth, exploded):
    if exploded:
        return
    if isinstance(node, Node):
        if node.is_leaf():
            return
        if node.depth >= 4:
            left_child = node.child1
            right_child = node.child2
            left_pos = order.index(left_child)
            if left_pos > 0:
                left_node = order[left_pos - 1]
                left_node.update_value(left_child.value + left_node.value)
            right_pos = order.index(right_child)
            if right_pos < len(order) - 1:
                right_node = order[right_pos + 1]
                right_node.update_value(right_child.value + right_node.value)
            node.update_value(0)
            node.child1 = None
            node.child2 = None
            exploded.append(node)
            return
        explode_node(node.child1, order, depth + 1, exploded)
        explode_node(node.child2, order, depth + 1, exploded)


def create_list_from_tree(node):
    if node is None:
        return
    if node.is_leaf():
        return node.value
    else:
        return [create_list_from_tree(node.child1)] + [create_list_from_tree(node.child2)]


def get_depth(node):
    if node is None:
        return 0
    if node.is_leaf():
        return 0
    return 1 + max(get_depth(node.child1), get_depth(node.child2))


def get_magnitude(root):
    if root.is_leaf():
        return root.value
    val1 = 0
    val2 = 0
    if root.child1 is not None:
        val1 = 3*get_magnitude(root.child1)
    if root.child2 is not None:
        val2 = 2*get_magnitude(root.child2)
    return val1 + val2


def reduce(line):
    root = Node(line)
    create_tree(root, line)
    while get_depth(root) > 4 or has_split(root):
        while get_depth(root) > 4:
            exploded = []
            order = []
            traverse_tree(root, order)
            explode_node(root, order, 0, exploded)
            line = create_list_from_tree(root)
            root.value = create_list_from_tree(root)
            create_tree(root, line)
        if split_node := has_split(root):
            low = math.floor(split_node.value / 2)
            high = math.ceil(split_node.value / 2)
            left_node = Node(low, split_node, split_node.depth+1)
            right_node = Node(high, split_node, split_node.depth+1)
            split_node.child1 = left_node
            split_node.child2 = right_node
            split_node.value = create_list_from_tree(split_node)
            line = create_list_from_tree(root)
            root.value = create_list_from_tree(root)
            create_tree(root, line)
    return root


root = reduce(data[0])
for i in range(len(data) - 1):
    b = reduce(data[i + 1])
    root = reduce([root.value] + [b.value])

print('Part 1: ', get_magnitude(root))

max_magnitude = 0

for first in data:
    for second in data:
        if first == second:
            continue
        a = reduce(first)
        b = reduce(second)
        total = reduce([first] + [second])
        magniutde = get_magnitude(total)
        if magniutde > max_magnitude:
            max_magnitude = magniutde

print('Part 2: ', max_magnitude)
