import sys
from functools import reduce
path = sys.argv[1] if len(sys.argv) > 1 else 'puzzle.txt'
with open(path) as file:
    data = file.readline().strip()


def parse_packet(packet):
    version_sum = 0
    version = int(packet[:3], 2)
    version_sum += version
    type = int(packet[3:6], 2)
    if type == 4:
        val = ""
        offset = 6
        while int(packet[offset], 2) == 1:
            val += packet[offset+1:offset+5]
            offset += 5
        val += packet[offset+1:offset+5]
        offset += 5
        total_length = offset
        value = int(val, 2)
    else:
        values = []
        length_id = int(packet[6], 2)
        if length_id == 1:
            subpacket_start = 7 + 11
            subpacket_count = int(packet[7:subpacket_start], 2)
            def comparator(): return current_packet < subpacket_count
        else:
            subpacket_start = 7 + 15
            subpacket_length = int(packet[7:subpacket_start], 2)
            def comparator(): return offset < subpacket_length + subpacket_start
        offset = subpacket_start
        current_packet = 0
        while comparator():
            length, ver, val = parse_packet(packet[offset:])
            version_sum += ver
            offset += length
            current_packet += 1
            values.append(val)
        total_length = offset

        if type == 0:
            value = sum(values)
        elif type == 1:
            value = reduce(lambda acc, x: x*acc, values, 1)
        elif type == 2:
            value = min(values)
        elif type == 3:
            value = max(values)
        elif type == 5:
            value = 1*(values[0] > values[1])
        elif type == 6:
            value = 1*(values[0] < values[1])
        elif type == 7:
            value = 1*(values[0] == values[1])

    return total_length, version_sum, value


packet = ''.join([f"{int(bin(int(x, 16))[2:]):04d}" for x in data])

_, part1, part2 = parse_packet(packet)
print('Part 1: ', part1)
print('Part 2: ', part2)
