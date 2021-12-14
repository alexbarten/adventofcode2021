def main():
    levels = map_levels_to_list("src/december09/test.txt")
    detect_low_levels(levels)


def map_levels_to_list(levels):
    levellist = []
    with open(levels, "r") as levels:
        for level in levels:
            level = level.replace("\n", "")
            levellist.append(list(level))

    return levellist


def detect_low_levels(levels):
    lowpoints = []
    lineno = 0
    for level in range(len(levels + 1)):
        for i in range(len(levels[0] + 1)):
            if lineno == 0:
                if i == 0:
                    if level[0][0] < level[0][1] and \
                       level[0][0] < level[1][0]:
                       lowpoints.append(0, 0, level[0][0])
                if i == len(levels):
                    if level[0][0] < level[0][1] and \
                       level[0][0] < level[1][0]:
                       lowpoints.append(0, 0, level[0][len(level)])


if __name__ == "__main__":
    main()
