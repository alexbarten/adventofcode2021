def main():
    codes, output_signals = clean_signals("src/december08/test.txt")
    sorted_codes = sort_codes(codes)
    numbers = assign_numbers_to_codes(sorted_codes)
    print(output_signals)
    # occurrences = calculate_digits(no_of_digits, digits_to_calculate)
    # print("The number of occurrences of 1, 4, 7, and 8 is ", occurrences)


def clean_signals(digits):
    with open(digits, "r") as digits:
        for signal in digits:
            signal = signal.replace("\n", "")
            codes, output_signals = signal.split(" | ")
            codes = codes.split(" ")
            output_signals = output_signals.split(" ")

    return codes, output_signals


def sort_codes(codes):
    sorted_codes = []
    for code in codes:
        chars = list(code)
        chars.sort()
        sorted_codes.append(''.join(chars))
    sorted_codes.sort(key=len)

    return(sorted_codes)


def assign_numbers_to_codes(codes):
    numbers = {}

    numbers[codes[0]] = 1
    numbers[codes[1]] = 7
    numbers[codes[2]] = 4
    numbers[codes[9]] = 8
    for i in range(3, 6):
        if codes[0] in codes[i]:
            numbers[codes[i]] = 3
    for j in range(6, 9):
        match = True
        for char in range(4):
            if codes[2][char] not in codes[j]:
                match = False
        if match:
            numbers[codes[j]] = 9
            for m in range(6, 9):
                if codes[j] != codes[m]:
                    charcount = 0
                    for char in range(6):
                        if codes[j][char] in codes[m]:
                            charcount += 1
                    if charcount == 5 and (codes[0] in codes[m]):
                        numbers[codes[m]] = 0
    for j in range(6, 9):
        if codes[j] not in numbers.keys():
            numbers[codes[j]] = 6
    for i in range(3, 6):
        charcounter = 0
        for char in range(4):
            if codes[2][char] in codes[i]:
                charcounter += 1
        if charcounter == 3 and codes[i] not in numbers.keys():
            numbers[codes[i]] = 5
        if charcounter == 2 and codes[i] not in numbers.keys():
            numbers[codes[i]] = 2

    return numbers


def calculate_digits(no_of_digits, digits_to_calculate):
    segments = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    total_digits = 0
    for digit in digits_to_calculate:
        total_digits += no_of_digits[segments.get(digit)]

    return total_digits


if __name__ == "__main__":
    main()
