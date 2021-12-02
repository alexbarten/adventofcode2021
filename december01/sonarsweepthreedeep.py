def main():
    compute_deeper_readings('december01/depths.txt')


def compute_deeper_readings(readings):
    deeper_readings = 0
    previous_window = 0
    window = 0
    i = 0
    windows = [0]

    with open(readings, 'r') as depths:
        for depth in depths:
            windows.extend([0, 0])
            windows[i] = windows[i] + int(depth)
            windows[i+1] = windows[i+1] + int(depth)
            windows[i+2] = windows[i+2] + int(depth)
            i += 1

    windows = windows[2:]
    for window in windows:
        if window > previous_window:
            deeper_readings += 1
        previous_window = window

    print("The number of deeper depth readings is: ", deeper_readings - 1)
    # We deduct one, to compensate for the first reading, which compared to
    # the initialized value of previous_depth.


if __name__ == "__main__":
    main()
