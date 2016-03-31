lines = '''
  +-+
  | |
+-+-+
| | |
+-+-+
'''

# lines = [
#     "  +-+",
#     "    |",
#     "+-+-+",
#     "| | -",
#     "+-+-+"
# ]

lines = [
    "  +-+",
    "    |",
    "+|+-+",
    "| | -",
    "+-+-+"
]


def count(string=''):
    count = 0
    if type(string) is str:
        lines = [s for s in string.split('\n') if s]
    else:
        lines = string
    rows = {'+': [], '|': []}
    lineNum = 0
    for line in lines:
        cornersInRow = [lineNum, ]
        sidesInRow = [lineNum, ]
        index = 0
        sides = set()
        corners = set()
        for c in line:
            if c == '+':
                corners.add(index)
            elif c == '|':
                sides.add(index)
            index += 1

        if corners:
            cornersInRow.append(corners)
            rows['+'].append(cornersInRow)
        if sides:
            sidesInRow.append(sides)
            rows['|'].append(sidesInRow)

        lineNum += 1

        # if len(row) > 1:
        #     tmp = row.copy()
        #     for i in tmp:
        #         if line[i] not in ('+', '|'):
        #             row.remove(i)
        #     count += len(row) * (len(row) - 1) / 2
        # else:
        #     index = 0
        #     row = set()
        #     for c in line:
        #         if c == '+':
        #             row.add(index)
        #         index += 1

    print rows
    # rows = len(sides)

    # for i in xrange(rows):
    #     for j in xrange(i, rows):
    #         if

    return count


print count(lines)
# print set([0, 2, 4]).difference(set([2, 4]))
