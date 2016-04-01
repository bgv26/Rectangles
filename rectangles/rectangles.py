lines = '''
  +--+
  |  |
+-+--+
| |  |
+-+--+
'''

# lines = ["+-+",
#          "| |",
#          "+-+",
#          ]
#
# lines = ["  +-+",
#          "  | |",
#          "+-+-+",
#          "| |  ",
#          "+-+  "
#          ]
#
# lines = ["  +-+",
#          "  | |",
#          "+-+-+",
#          "| | |",
#          "+-+-+"
#          ]
#
# lines = ["  +-+",
#          "    |",
#          "+-+-+",
#          "| | -",
#          "+-+-+"
#          ]
#
# lines = ["+------+----+",
#          "|      |    |",
#          "+---+--+    |",
#          "|   |       |",
#          "+---+-------+"
#          ]
#
lines = ["+------+----+",
         "|      |    |",
         "+------+    |",
         "|   |       |",
         "+---+-------+"
         ]


def get_horizontal_sides(string=''):
    rectangles = []
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
                        down_side = get_rectangle(lines, line_num, offset, length)
                        if down_side:
                            rectangles.append((line_num, offset, length, down_side))
                    offset = length
        line_num += 1
    return rectangles


def get_rectangle(lines, line_num, start, end):
    if line_num < len(lines) - 1:
        line_num += 1
    else:
        return 0
    while True:
        left_side = lines[line_num][start]
        right_side = lines[line_num][end]
        if  left_side == '|' and right_side == '|':
            if line_num < len(lines) - 1:
                line_num += 1
            else:
                return 0
        elif left_side == '+' and right_side == '+':
            return line_num
        else:
            return 0

print get_horizontal_sides(lines)

def get_side(string = ''):
    if type(string) is str:
        lines = [s for s in string.split('\n') if s]
    else:
        lines = string
    for line in lines:
        left = line.find('+')
        if left >= 0:
            left += 1
            while line[left] == '-':
                left += 1
#                 регулярочка "\+(\-+)(?=\+)"

print get_side(lines)