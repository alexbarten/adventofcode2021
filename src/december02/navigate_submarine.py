def main():
    compute_submarine_position('src/december02/course.txt')


def compute_submarine_position(course):
    horizontal_position = 0
    depth = 0

    with open(course, 'r') as navigation_units:
        for navigation_unit in navigation_units:
            direction, amount = navigation_unit.split()
            if direction == "forward":
                horizontal_position += int(amount)
            elif direction == "down":
                depth += int(amount)
            elif direction == "up":
                depth -= int(amount)
            else:
                print("You are trying me, aren't you?")

    print("Final horizontal position = ", horizontal_position)
    print("Final depth = ", depth)
    print("Computed position = ", horizontal_position * depth)


if __name__ == "__main__":
    main()
