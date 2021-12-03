# Advent of Code 2021

This repo contains Python solutions to the [Advent of Code 2021](https://adventofcode.com/2021/)

## My own additional challenge

1. I use Python 3.9.9, but I am not allowed to use any additional libraries, neither standard libraries, nor third party libraries.
2. I must write readable Python. It is all about being understandable without documentation.

## Puzzles

### December 1

#### Challenge 1 - Sonar Sweep

The input consists of a list of numbers.

When the next number is higher than the presceding number, we count. If not, we do not count.

The result is the number of times that the next number is higher than the previous number.

#### Challenge 2 - Sonar Sweep using windows

We re-use the input of challenge 1. Instead, we need to compare windows of three consecutive numbers with the next window. Windows move by 1 (so there are always two overlapping values with the former window). We count all windows that have a higher value (i.e. deeper sea floor).

### December 3

#### Challenge 1 - Determine the power consumption of the submarine

Read the data from a file with binary numbers. It has 12 columns. Determine for each bit-column if it is generally set, or unset. Construct a new binary number from the results.

Then construct a binary number that has the opposite binary values.

Now convert both numbers to decimal, and multiply these. The result is the power consumption of the submarine.

#### Challenge 2 - Verify the life support rating

Read the data from a file with binary numbers. It has 12 columns. Determine for the first bit-column if it is set, or unset. Keep the numbers of each result together in a new set. Now filter again, on the second column, still on the 1 in set 1, and on the zero in set 2.

In the end we end up with two numbers. Multiply these to get the life support rating.
