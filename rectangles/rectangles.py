import re


def count(string=''):
    if type(string) is str:
        lines = [s for s in string.split('\n') if s]
    else:
        lines = string
    rectangles = {}
    line_num = 0
    for line in lines:
        hor_side = re.compile(r"(?<=\+)(-*)(?=\+)")
        matches = [(match.start(), match.end()) for match in hor_side.finditer(line)]
        sides = len(matches)
        for i in range(sides):
            right_end = matches[i][1]
            for j in range(i + 1, sides):
                if right_end + 1 == matches[j][0]:
                    matches.append((matches[i][0], matches[j][1]))
                    right_end = matches[j][1]
        if matches:
            rectangles[line_num] = matches
        line_num += 1

    num_of_rectangles = 0
    line_num = rectangles.keys()
    hor_side_num = len(line_num)
    for i in range(hor_side_num):
        for j in range(i + 1, hor_side_num):
            upside_num = line_num[i]
            downside_num = line_num[j]
            for up_side in rectangles[upside_num]:
                if up_side in rectangles[downside_num]:
                    num_of_rectangles += get_rectangle(lines, upside_num, downside_num, up_side)

    return num_of_rectangles


def get_rectangle(lines, upside_num, downside_num, up_side):
    start = up_side[0] - 1
    end = up_side[1]
    for i in range(upside_num + 1, downside_num):
        if lines[i][start] not in ('|', '+') or lines[i][end] not in ('|', '+'):
            return 0

    return 1
