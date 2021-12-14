def main():
    potentially_invalid_chunks = \
        determine_potential_errorlines("src/december10/test.txt")
    parse_errors(potentially_invalid_chunks)


def determine_potential_errorlines(chunksfile):
    potentially_invalid_chunks = []
    with open(chunksfile, "r") as chunks:
        for chunkline in chunks:
            chunkline = chunkline.rstrip()
            if chunkline[-1:] not in "([{<":
                potentially_invalid_chunks.append(chunkline)

    return potentially_invalid_chunks


def parse_errors(potentially_invalid_chunks):
    for chunklines in potentially_invalid_chunks:
        chars = potentially_invalid_chunks[chunklines].split()
        for char in chars:
            if chars[char] == "(" and chars[char + 1] == ")" or\
               chars[char] == "[" and chars[char + 1] == "]" or\
               chars[char] == "{" and chars[char + 1] == "}" or\
               chars[char] == "<" and chars[char + 1] == ">":
                print(chars[char], chars[char + 1])


if __name__ == "__main__":
    main()
