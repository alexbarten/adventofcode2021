# Advent of Code 2021

This repo contains Python solutions to the [Advent of Code 2021](https://adventofcode.com/2021/)

## Puzzles

### December 1

#### Challenge 1 - Sonar Sweep

The input consists of a list of numbers.

When the next number is higher than the presceding number, we count. If not, we do not count.

The result is the number of times that the next number is higher than the previous number.

#### Challenge 2 - Sonar Sweep using windows

We re-use the input of challenge 1. Instead, we need to compare windows of three consecutive numbers with the next window. Windows move by 1 (so there are always two overlapping values with the former window). We count all windows that have a higher value (i.e. deeper sea floor).
