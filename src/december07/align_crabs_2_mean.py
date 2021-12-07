def main():
    crabs = crabs_to_list("src/december07/test.txt")
    mean = determine_mean(crabs)
    steps = calculate_steps(crabs, mean)
    # print(crabs)
    print(mean)
    print(steps)


def crabs_to_list(crabsfile):
    crabs_file = open(crabsfile, "r")
    crabs_line = crabs_file.readline().replace("\n", "")
    crabs = crabs_line.split(",")
    crabs = list(map(int, crabs))

    return crabs


def determine_mean(crabs):
    mean = int(sum(crabs) / len(crabs))
    a = (sum(crabs) / len(crabs))
    print("non-int mean is ", a)
    if sum(crabs) % len(crabs) != 0:
        mean += 1

    return mean


def calculate_steps(crabs, mean):
    steps = 0
    for crab in crabs:
        for i in range(1, (abs(crab - mean) + 1)):
            steps += i

    return steps


if __name__ == "__main__":
    main()
