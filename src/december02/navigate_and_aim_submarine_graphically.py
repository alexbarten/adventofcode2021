import turtle


def main():
    compute_submarine_position('course.txt')


def compute_submarine_position(course):
    horizontal_position = 0
    aim = 0
    depth = 0
    submarine_.penup()
    submarine_.setposition(-500, 350)
    submarine_.pendown()
    submarine_.speed('fastest')

    with open(course, 'r') as navigation_units:
        for navigation_unit in navigation_units:
            direction, amount = navigation_unit.split()
            amount = int(amount)
            if direction == "forward":
                horizontal_position += amount
                depth += amount * aim
                submarine_.setheading(0)
                submarine_.forward(amount)
                submarine_.setheading(270)
                submarine_.forward(amount * aim)
            elif direction == "down":
                aim += amount
            elif direction == "up":
                aim -= amount
            else:
                print("You are trying me, aren't you?")

    print("Final horizontal position = ", horizontal_position)
    print("Final depth = ", depth)
    print("Computed position = ", horizontal_position * depth)

    turtle.done()


submarine_ = turtle.Turtle()
submarine_.screen.setworldcoordinates(-500, -1000000, 1500, 0)

if __name__ == "__main__":
    main()
