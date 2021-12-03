def main():
    determine_powerconsumption('src/december03/diagnostics.txt')


def determine_powerconsumption(diagnostics):
    counter = [0] * 24
    position = 0
    with open(diagnostics, 'r') as diagnostics:
        for diagnostic in diagnostics:
            for position in range(12):
                if diagnostic[position:position + 1] == "1":
                    counter[position] += 1
                else:
                    counter[position + 12] += 1

    gamma_rate_binary = [0] * 12
    for position in range(12):
        if counter[position] >= counter[position + 12]:
            gamma_rate_binary[position] = 1

    gamma_rate = ''.join(map(str, gamma_rate_binary))
    flipbinary = gamma_rate.replace('1', 'p')
    flipbinary = flipbinary.replace('0', '1')
    epsilon_rate = flipbinary.replace('p', '0')

    print("The power consumption of the submarine is ",
          int(gamma_rate, 2) * int(epsilon_rate, 2))


if __name__ == "__main__":
    main()
