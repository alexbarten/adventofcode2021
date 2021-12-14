def main():
    draws, house_of_cards = extract_bingofile("src/december04/bingo.txt")
    for current_round in draws.draw_sequence:
        draw, the_end = draws.emit_draw()
        if the_end:
            print("Game Over. We have no winner...")

        for bingocard in house_of_cards:
            bingocard.compute_draw(draw)
            bingocard.we_have_a_winner()
            if bingocard.response > 0:
                bingocard.determine_score(draw)
                print("The score of the winning card is ", bingocard.score)


class draw:
    def __init__(self, draw_sequence):
        string_sequence = draw_sequence.split(",")
        self.draw_sequence = list(map(int, string_sequence))
        self.current_draw = 0
        self.sequence_end = False

    def emit_draw(self):
        if len(self.draw_sequence) > self.current_draw:
            self.current_draw += 1
        else:
            self.sequence_end = True

        return self.draw_sequence[self.current_draw - 1], self.sequence_end


class bingocard:
    def __init__(self, board):
        self.card = board

    def compute_draw(self, draw):
        for row in range(5):
            for column in range(5):
                if self.card[row][column] == draw:
                    self.card[row][column] = 0
        return draw

    def we_have_a_winner(self):
        self.response = 0
        for row in range(5):
            if sum(self.card[row]) == 0:
                self.response = 1

        for column in range(5):
            column_sum = 0
            for row in range(5):
                column_sum = column_sum + self.card[row][column]
            if column_sum == 0:
                self.response = 2

    def determine_score(self, draw):
        self.score = 0
        for row in range(5):
            self.score = self.score + sum(self.card[row])
        self.score = self.score * draw


def extract_bingofile(bingofile):
    with open(bingofile, "r") as bingofile:
        line = bingofile.readline().replace("\n", "")
        draws = draw(line)  # First line contains draws.
        bingofile.readline()  # Read second, empty line, to skip it.

        card = []
        house_of_cards = []
        for line in bingofile:
            if line != "\n":
                line = line.replace("\n", "").split(" ")
                int_line = []
                for item in line:
                    if item != "":
                        int_line.append(int(item))
                card.append(int_line)
            else:
                house_of_cards.append(bingocard(card))
                card = []

    return draws, house_of_cards


if __name__ == "__main__":
    main()
