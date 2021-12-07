def main():
    fishschool = fishschool_to_list("src/december06/fish.txt")
    grown_school = reduce_and_grow(fishschool, 80)
    print("The number of fish is ", len(grown_school))


def fishschool_to_list(file):
    fishschoolfile = open(file, "r")
    fishschool_line = fishschoolfile.readline().replace("\n", "")
    fishschool = []
    for fish in fishschool_line:
        if fish != ",":
            fishschool.append(int(fish))

    return fishschool


def reduce_and_grow(fishschool, days):
    for day in range(days):
        fishcounter = 0
        baby_fish = 0
        for fish in fishschool:
            fishschool[fishcounter] -= 1
            if fishschool[fishcounter] < 0:
                fishschool[fishcounter] = 6
                baby_fish += 1
            fishcounter += 1
        for baby in range(baby_fish):
            fishschool.append(8)

    return fishschool


if __name__ == "__main__":
    main()
