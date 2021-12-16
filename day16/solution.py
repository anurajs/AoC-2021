import sys
path = sys.argv[1] if len(sys.argv) > 1 else 'puzzle.txt'
with open(path) as file:
    data = file.readline().strip()


def parse_packet(packet):
    version_sum = 0
    version = int(packet[:3], 2)
    version_sum += version
    type = int(packet[3:6], 2)
    offset = 6
    if type == 4:
        value = ""
        while packet[offset] == '1':
            value += packet[offset+1:offset+5]
            offset += 5
        value += packet[offset+1:offset+5]
        offset += 5
        total_length = offset
        value = int(value, 2)
    else:
        values = []
        length_id = int(packet[6], 2)
        if length_id == 1:
            subpacket_start = 7 + 11
            subpacket_count = int(packet[7:subpacket_start], 2)
            offset = subpacket_start
            current_packet = 0
            while current_packet < subpacket_count:
                length, ver, val = parse_packet(packet[offset:])
                version_sum += ver
                offset += length
                current_packet += 1
                values.append(val)
        else:
            subpacket_start = 7 + 15
            subpacket_length = int(packet[7:subpacket_start], 2)
            offset = subpacket_start
            while offset < subpacket_length + subpacket_start:
                length, ver, val = parse_packet(packet[offset:])
                version_sum += ver
                offset += length
                values.append(val)
        total_length = offset
        if type == 0:
            value = sum(values)
        elif type == 1:
            value = 1
            for v in values:
                value *= v
        elif type == 2:
            value = min(values)
        elif type == 3:
            value = max(values)
        elif type == 5:
            value = 1 if values[0] > values[1] else 0
        elif type == 6:
            value = 1 if values[0] < values[1] else 0
        elif type == 7:
            value = 1 if values[0] == values[1] else 0
    return total_length, version_sum, value


hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

packet = ''.join([hex_to_bin[x] for x in data])

_, part1, part2 = parse_packet(packet)
print('Part 1: ', part1)
print('Part 2: ', part2)
