def main():
    deeper_readings = 0
    previous_depth = 0

    with open('depths.txt', 'r') as depths:
        depth = depths.readline()
        if previous_depth != 0:
            if depth > previous_depth:
                deeper_readings += 1
        previous_depth = depth

    depths.close()


if __name__ == "__main__":
    main()
