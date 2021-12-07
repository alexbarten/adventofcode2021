def main():
    coordinates = clean_input("src/december05/input.txt")
    filtered_list = filter_relevant_pairs(coordinates)
    dangerous_points = plot_lines(filtered_list)
    print("The number of dangerous points is ", len(dangerous_points))


def clean_input(input):
    all_coordinates = []
    with open(input, "r") as pairs_of_points:
        for pair_of_points in pairs_of_points:
            pair_of_points = pair_of_points.replace("\n", "")\
                .replace(" -> ", ",")
            pair_of_points = pair_of_points.split(",")
            pair_of_points = list(map(int, pair_of_points))
            all_coordinates.append(pair_of_points)

    return all_coordinates


def filter_relevant_pairs(coordinates):
    filtered_list = []
    for points in coordinates:
        if points[0] == points[2]:
            if points[1] > points[3]:
                points[1], points[3] = points[3], points[1]
            filtered_list.append(points)
        if points[1] == points[3]:
            if points[0] > points[2]:
                points[0], points[2] = points[2], points[0]
            filtered_list.append(points)

    return filtered_list


def plot_lines(list_of_coordinates):
    board = [[0 for x in range(999)] for y in range(999)]
    dangerous_points = []

    for points in list_of_coordinates:
        if points[0] != points[2]:
            for x in range(points[0], points[2] + 1):
                board[x][points[1]] += 1
                if board[x][points[1]] == 2:
                    dangerous_points.append([x, points[1]])
        else:
            for y in range(points[1], points[3] + 1):
                board[points[0]][y] += 1
                if board[points[0]][y] == 2:
                    dangerous_points.append([points[0], y])

    return dangerous_points


if __name__ == "__main__":
    main()
