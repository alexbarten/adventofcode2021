def main():
    compute_deeper_readings('december01/depths.txt')


def compute_deeper_readings(readings):
    deeper_readings = 0
    previous_depth = 0

    with open(readings, 'r') as depths:
        for depth in depths:
            if int(depth) > previous_depth:
                deeper_readings += 1
            previous_depth = int(depth)

    print("The number of deeper depth readings is: ", deeper_readings - 1)
    # We deduct one, to compensate for the first reading, which compared to
    # the initialized value of previous_depth.


if __name__ == "__main__":
    main()
