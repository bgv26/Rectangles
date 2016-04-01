lines = '''
  +--+
  |  |
+-+--+
| |  |
+-+--+
'''

lines = ["+-+",
         "| |",
         "+-+",
         ]

lines = ["  +-+",
         "  | |",
         "+-+-+",
         "| |  ",
         "+-+  "
         ]

lines = ["  +-+",
         "  | |",
         "+-+-+",
         "| | |",
         "+-+-+"
         ]

lines = ["  +-+",
         "    |",
         "+-+-+",
         "| | -",
         "+-+-+"
         ]

lines = ["+------+----+",
         "|      |    |",
         "+---+--+    |",
         "|   |       |",
         "+---+-------+"
         ]

lines = ["+------+----+",
         "|      |    |",
         "+------+    |",
         "|   |       |",
         "+---+-------+"
         ]


def get_horizontal_sides(string=''):
    horizontal_sides = {}
    if type(string) is str:
        lines = [s for s in string.split('\n') if s]
    else:
        lines = string
    line_num = 0
    for line in lines:
        tmp = line.split('+')
        if len(tmp) > 2:
            offset = 0
            first = True
            for s in tmp:
                length = len(s)
                if first:
                    offset += length
                    first = False
                else:
                    length += offset + 1
                    if len(set(s)) == 1 and '-' in s:
                        if horizontal_sides.get(line_num, 0):
                            horizontal_sides[line_num].append([offset, length])
                        else:
                            horizontal_sides[line_num] = [[offset, length]]
                    offset = length
        line_num += 1
    return horizontal_sides


def check_vertical_sides(string=''):
    count = 0
    if type(string) is str:
        lines = [s for s in string.split('\n') if s]
    else:
        lines = string

    horizontal_sides = get_horizontal_sides(string)
    print horizontal_sides

    horizontal_num_lines = set(horizontal_sides.keys())

    vertical_num_lines = set(range(len(lines))).difference(horizontal_num_lines)

    for num in horizontal_sides:
        for side in horizontal_sides[num]:
            start = side[0]
            end = side[1]
            if num:
                if lines[num-1][start] in ('|','+') and lines[num-1][end] in ('|', '+'):
                    count += 1
            else:
                if lines[num+1][start] in ('|','+') and lines[num+1][end] in ('|', '+'):
                    count += 1

    return count
            # for i in vertical_num_lines:
            #     upLine =
            #     tmp =lines[i].split('|')


print check_vertical_sides(lines)

# def count(string=''):
#     count = 0
#     if type(string) is str:
#         lines = [s for s in string.split('\n') if s]
#     else:
#         lines = string
#     rows = {'+': [], '|': []}
#     lineNum = 0
#     for line in lines:
#         cornersInRow = [lineNum, ]
#         sidesInRow = [lineNum, ]
#         index = 0
#         sides = set()
#         corners = set()
#         for c in line:
#             if c == '+':
#                 corners.add(index)
#             elif c == '|':
#                 sides.add(index)
#             index += 1
#
#         if corners:
#             cornersInRow.append(corners)
#             rows['+'].append(cornersInRow)
#         if sides:
#             sidesInRow.append(sides)
#             rows['|'].append(sidesInRow)
#
#         lineNum += 1
#
#         # if len(row) > 1:
#         #     tmp = row.copy()
#         #     for i in tmp:
#         #         if line[i] not in ('+', '|'):
#         #             row.remove(i)
#         #     count += len(row) * (len(row) - 1) / 2
#         # else:
#         #     index = 0
#         #     row = set()
#         #     for c in line:
#         #         if c == '+':
#         #             row.add(index)
#         #         index += 1
#
#     print rows
#     # rows = len(sides)
#
#     # for i in xrange(rows):
#     #     for j in xrange(i, rows):
#     #         if
#
#     return count
#
#
# print count(lines)
# # print set([0, 2, 4]).difference(set([2, 4]))
