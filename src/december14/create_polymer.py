def main():
    steps = 40
    template, pair_insertion_rules = convert_rules("src/december14/test.txt")
    polymer = create_polymer(template, pair_insertion_rules, steps)
    advent_result = calculate_occurrences(polymer)
    print("The maximum - minimum number of chars = ", advent_result)


def convert_rules(polymer_template):
    with open(polymer_template, "r") as polymers:
        template = polymers.readline().rstrip()
        polymers.readline()
        pair_insertion_rules = {}
        for pair_insertion_rule in polymers:
            line = pair_insertion_rule.replace(" -> ", " ").rstrip()
            key, value = line.split()
            pair_insertion_rules.update({key: value})

    return (template, pair_insertion_rules)


def create_polymer(template, pair_insertion_rules, steps):
    for step in range(steps):
        created_polymer = ""
        for position in range(len(template) - 1):
            pair = template[position: position + 2]
            if pair in pair_insertion_rules:
                char = pair_insertion_rules.get(pair)
                created_polymer += pair[0:1]
                created_polymer += char
        created_polymer += pair[1:2]
        template = created_polymer

    return created_polymer


def calculate_occurrences(polymer):
    charcounter = {}
    for char in list(set(polymer)):
        counter = polymer.count(char)
        charcounter.update({char: counter})

    return max(charcounter.values()) - min(charcounter.values())


if __name__ == "__main__":
    main()
