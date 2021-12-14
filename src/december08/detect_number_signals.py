def main():
    no_of_digits = count_signals("src/december08/digits.txt")
    digits_to_calculate = [1, 4, 7, 8]
    occurrences = calculate_digits(no_of_digits, digits_to_calculate)
    print("The number of occurrences of 1, 4, 7, and 8 is ", occurrences)


def count_signals(digits):
    no_of_digits = [0] * 9
    with open(digits, "r") as digits:
        for signal in digits:
            signal = signal.replace("\n", "")
            output_signals = signal.split(" | ")[1].split(" ")
            for signal in output_signals:
                no_of_digits[len(signal)] += 1

    return no_of_digits


def calculate_digits(no_of_digits, digits_to_calculate):
    segments = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    total_digits = 0
    for digit in digits_to_calculate:
        total_digits += no_of_digits[segments.get(digit)]

    return total_digits


if __name__ == "__main__":
    main()
