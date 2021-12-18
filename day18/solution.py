import sys
import math
from collections import defaultdict
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
        if parent is None:
            self.depths = defaultdict(lambda: 0)
            self.depths[0] = 1
        else:
            self.depths = parent.depths
            self.depths[depth] += 1

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
        self.parent.update_value(
            [self.parent.child1.value] + [self.parent.child2.value])


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
    if node is not None:
        traverse_tree(node.child1, order)
        if node.is_leaf():
            order.append(node)
        traverse_tree(node.child2, order)


def has_split(node):
    if node is not None:
        if node.is_leaf() and node.value > 9:
            return node
        return has_split(node.child1) or has_split(node.child2)


def explode_node(node, order, depth, exploded):
    if exploded:
        return
    if node is not None:
        if node.is_leaf():
            return
        if node.depth >= 4:
            left_child = node.child1
            right_child = node.child2
            left_pos = order.index(left_child)
            if left_pos > 0:
                left_node = order[left_pos - 1]
                left_node.update_value(left_child.value + left_node.value)
                order[left_pos - 1] = left_node
            right_pos = order.index(right_child)
            if right_pos < len(order) - 1:
                right_node = order[right_pos + 1]
                right_node.update_value(right_child.value + right_node.value)
                order[right_pos + 1] = right_node
            node.update_value(0)
            node.depths[depth] -= 1
            node.depths[left_child.depth] -= 1
            node.depths[right_child.depth] -= 1
            node.child1 = None
            node.child2 = None
            order[left_pos] = node
            order.remove(right_child)
            exploded.append(True)
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


def find_splittable(order):
    for index, item in enumerate(order):
        if item.value > 9:
            return index
    return -1


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
    order = []
    traverse_tree(root, order)
    while root.depths[5] > 0 or find_splittable(order) != -1:
        while root.depths[5] > 0:
            exploded = []
            explode_node(root, order, 0, exploded)
        idx = find_splittable(order)
        if idx != -1:
            split_node = order[idx]
            low = math.floor(split_node.value / 2)
            high = math.ceil(split_node.value / 2)
            left_node = Node(low, split_node, split_node.depth+1)
            right_node = Node(high, split_node, split_node.depth+1)
            order[idx] = left_node
            order.insert(idx + 1, right_node)
            split_node.child1 = left_node
            split_node.child2 = right_node
            split_node.update_value([left_node.value] + [right_node.value])
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
