def main():
    determine_life_support_rating('src/december03/diagnostics.txt')


def determine_life_support_rating(diagnostics):
    oxygen_generator_rating = 0
    co2_scrubber_rating = 0
    list1 = []
    list0 = []
    file = open(diagnostics, 'r')
    diagnostic_lines = file.readlines()
    diagnostic_lines.sort()
    for i in range(len(diagnostic_lines)):
        if diagnostic_lines[i][0:1] == "1":
            list1.append(diagnostic_lines[i])
        else:
            list0.append(diagnostic_lines[i])

    for position in range(12):
        filter_most_occurring(list1, position, 1)

    for position in range(12):
        filter_most_occurring(list0, position, 0)

    print(list1)
    print(list0)
    # print("The life support rating of the submarine is ",
    #       int(co2_scrubber_rating, 2) * int(oxygen_generator_rating, 2))


def filter_most_occurring(mylist, position, prio):
    counter1 = 0
    counter0 = 0
    for diagnostic in mylist:
        if diagnostic[position:position + 1] == "1":
            counter1 += 1
        else:
            counter0 += 1

    if prio == 1:
        if counter1 >= counter0:
            minority_number = "0"
        else:
            minority_number = "1"
    else:
        if counter1 >= counter0:
            minority_number = "1"
        else:
            minority_number = "0"

    line_no = 0
    for minority_item in (mylist):
        if minority_item[position:position + 1] == minority_number:
            del mylist[line_no]
        line_no += 1


if __name__ == "__main__":
    main()

# answer is 6677951
