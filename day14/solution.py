from collections import defaultdict
import sys
path = sys.argv[1] if len(sys.argv) > 1 else 'puzzle.txt'
with open(path) as file:
    data = file.readlines()

template = data[0].strip()
rules = dict()
for rule in data[2:]:
    rule = rule.strip().split(' -> ')
    rules[rule[0]] = rule[1]


def get_counts(template, rules, amount):
    rule_counts = defaultdict(lambda: 0)
    for i in range(1, len(template)):
        rule = template[i-1:i+1]
        rule_counts[rule] += 1

    for _ in range(amount):
        new_rule_counts = defaultdict(lambda: 0)
        for rule, count in rule_counts.items():
            output = rules[rule]
            rule1 = rule[:1] + output
            rule2 = output + rule[1:]
            new_rule_counts[rule1] += count
            new_rule_counts[rule2] += count
        rule_counts = new_rule_counts

    counts = defaultdict(lambda: 0)
    ends = {template[0], template[-1]}

    for rule in rule_counts:
        counts[rule[:1]] += rule_counts[rule]
        counts[rule[1:]] += rule_counts[rule]

    for letter, count in counts.items():
        counts[letter] = (count + 1*(letter in ends)) // 2
    return counts


counts = get_counts(template, rules, 10)
max_char = max(counts, key=lambda x: counts[x])
min_char = min(counts, key=lambda x: counts[x])
print('Part 1: ', counts[max_char] - counts[min_char])

counts = get_counts(template, rules, 40)
max_char = max(counts, key=lambda x: counts[x])
min_char = min(counts, key=lambda x: counts[x])
print('Part 2: ', counts[max_char] - counts[min_char])
