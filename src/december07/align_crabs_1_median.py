def main():
    crabs = crabs_to_list("src/december07/crabs.txt")
    median = determine_median(crabs)
    steps = calculate_steps(crabs, median)
    # print(crabs)
    print(median)
    print(steps)


def crabs_to_list(crabsfile):
    crabs_file = open(crabsfile, "r")
    crabs_line = crabs_file.readline().replace("\n", "")
    crabs = crabs_line.split(",")
    crabs = list(map(int, crabs))
    crabs.sort()

    return crabs


def determine_median(crabs):
    if len(crabs) % 2 > 0:
        median = crabs[int(len(crabs) / 2)]
    else:
        below_median = crabs[(int(len(crabs) / 2) - 1)]
        above_median = crabs[(int(len(crabs) / 2))]
        median = int((below_median + above_median) / 2)

    return median


def calculate_steps(crabs, median):
    steps = 0
    for crab in crabs:
        steps += abs(crab - median)

    return steps


if __name__ == "__main__":
    main()
