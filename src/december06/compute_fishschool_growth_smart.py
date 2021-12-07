def main():
    fishschool = fishschool_to_dict("src/december06/fish.txt")
    grown_school = reduce_and_grow(fishschool, 256)
    number_of_fish = 0
    for value in grown_school.values():
        number_of_fish += value
    print("The number of fish is ", number_of_fish)

def fishschool_to_dict(file):
    fishschoolfile = open(file, "r")
    fishschool_line = fishschoolfile.readline().replace("\n", "")
    fishschool = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                  5: 0, 6: 0, 7: 0, 8: 0}
    for fish in fishschool_line:
        if fish != ",":
            fishschool[int(fish)] += 1

    return fishschool


def reduce_and_grow(fishschool, days):
    for day in range(days):
        new_babies = fishschool[0]
        for i in range(8):
            fishschool[i] = fishschool[i + 1]
        fishschool[8] = new_babies
        fishschool[6] += new_babies

    return fishschool


if __name__ == "__main__":
    main()
