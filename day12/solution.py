from collections import defaultdict

path = 'puzzle.txt'
with open(path) as file:
    data = file.readlines()


def traverse(node, path, edgeList, paths, visited, smalled):
    if node == 'end':
        paths.append(path)
        return
    for con in edgeList[node]:
        small = smalled
        if con == 'start':
            continue
        if con in visited and con.islower():
            if smalled:
                continue
            else:
                small = True
        traverse(con, [*path, con], edgeList, paths, {*visited, con}, small)
    return paths


edgeList = defaultdict(lambda: set())
for edges in data:
    edges = edges.strip().split('-')
    start, end = edges
    edgeList[start].add(end)
    edgeList[end].add(start)

part1 = traverse('start', ['start'], edgeList, [], {'start'}, True)
part2 = traverse('start', ['start'], edgeList, [], {'start'}, False)

print('Part 1: ', len(part1))
print('Part 2: ', len(part2))
