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
        if points[1] > points[3] and points[0] == points[2]:
            points[1], points[3] = points[3], points[1]
        if points[0] > points[2] and points[1] == points[3]:
            points[0], points[2] = points[2], points[0]
        if points[0] == points[2] or points[1] == points[3]:
            filtered_list.append(points)
        if abs(points[2] - points[0]) == abs(points[3] - points[1]):
            filtered_list.append(points)

    return filtered_list


def plot_lines(list_of_coordinates):
    board = [[0 for x in range(999)] for y in range(999)]
    dangerous_points = []

    for points in list_of_coordinates:
        if points[1] == points[3] and points[0] != points[2]:
            for x in range(points[0], points[2] + 1):
                board[x][points[1]] += 1
                if board[x][points[1]] == 2:
                    dangerous_points.append([x, points[1]])
        elif points[0] == points[2] and points[1] != points[3]:
            for y in range(points[1], points[3] + 1):
                board[points[0]][y] += 1
                if board[points[0]][y] == 2:
                    dangerous_points.append([points[0], y])
        else:
            if points[0] < points[2]:
                stepx = 1
                points[2] += 1
            else:
                stepx = -1
                points[2] -= 1
            y = points[1]
            if points[1] < points[3]:
                stepy = 1
            else:
                stepy = -1
            for x in range(points[0], points[2], stepx):
                board[x][y] += 1
                if board[x][y] == 2:
                    dangerous_points.append([x, y])
                y += stepy

    return dangerous_points


if __name__ == "__main__":
    main()
