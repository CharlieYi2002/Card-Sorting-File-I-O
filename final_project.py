# NAME: <Charlie Yi>
# ID: <5959558329>
# DATE: 2022-12-05
# DESCRIPTION: <Given a .txt file with each line containing a set of 5 cards,
# this program that will sort the cards from smallest to largest and output
# it into a new .txt file. The order of hierarchy is Ace, 2, 3, 4, ..., Jack, Queen,
# King. Cards of the same value will be compared by suit (Spade, Clover,
# Diamond, Heart).>

from typing import IO, Dict, List


# Card class
class Card:

    # constructor
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

    # Compares 2 cards and returns True is self is greater or equal, false otherwise
    def is_bigger(self, v, s):
        if self.val == v:
            return self.compare_suit(s)
        if self.val > v:
            return True
        return False

    # Compares the suit of 2 cards and returns True if the self.suit is bigger or equal, false otherwise
    # Order of suits from lowest to greatest is: Spade, Clover, Diamond, Heart
    def compare_suit(self, s):
        # dictionary to map values to suit in order of hierarchy
        suits = {'S': 1, 'C': 2, 'D': 3, 'H': 4}
        curr = int(suits[self.suit])
        other = int(suits[s])
        # (curr)
        if curr >= other:
            return True
        return False

    def __str__(self):
        return str(self.val) + str(self.suit)


# Open the file, checking for a valid input file name
# Return pointer to the file
def open_file() -> IO:
    file_pointer = None
    while file_pointer is None:
        file_pointer = input("Enter the name of the input file: ")
        try:
            file_pointer = open(file_pointer)
        except FileNotFoundError:
            print("File does not exist")
            file_pointer = None
    return file_pointer


# Read in the file and return a matrix of all the cards in the file
def read_file(input_file_pointer: IO) -> List[List[str]]:
    content = []

    # iterate through the file
    counter = 0
    for line in input_file_pointer:
        content.append([])
        card = line.strip().split(" ")

        # Declare each card
        for i in range(0, len(card)):
            content[counter].append(declare_card(card[i]))
        counter += 1

    # print(content)
    """
    for i in range(0, len(content)):
        for j in range(0, len(content[i])):
            print(content[i][j], end = " ")
        print()
    """
    input_file_pointer.close()

    return content


# write the new contents into the user given output file
def write_file(content: List[List[Card]]) -> None:
    file_name = input("Please enter the filename: ")
    wf = open(file_name, "w")
    # dictionary mapping values to royals/aces
    royals = {1: "A", 11: "J", 12: "Q", 13: "K"}
    for i in range(0, len(content)):
        for j in range(0, len(content[i])):
            # check if the value maps to a royal or ace
            if content[i][j].val == 1 or content[i][j].val > 10:
                wf.write(royals[content[i][j].val] + content[i][j].suit + " ")
            else:
                wf.write(str(content[i][j].val) + content[i][j].suit + " ")
        wf.write("\n")


# This function checks for royals and aces and converts them into numeric values,
# then instantiate/return a card object
def declare_card(s: str) -> Card(int, str):
    val = s[0]
    suit = s[-1]

    # check for royals and aces
    if val.isalpha():
        if val == 'J':
            val = 11
        if val == 'Q':
            val = 12
        if val == 'K':
            val = 13
        if val == 'A':
            val = 1
    # print(val)
    return Card(int(val), suit)


# this function calls the bubble_sort function while iterating through each row of the matrix
def sort(content) -> List[List[Card]]:
    for i in range(len(content)):
        bubble_sort(content[i])

    """
    for i in range(0, len(content)):
        for j in range(0, len(content[i])):
            print(content[i][j], end=" ")
        print()
    """


# sort the array recursively using bubble sort
def bubble_sort(arr):
    n = len(arr)
    swap = False
    # print("here")

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            # compare using card classes built-in comparison function
            if arr[j].is_bigger(arr[j + 1].val, arr[j + 1].suit):
                swap = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # if swap is false, then traverse back the recursive function
        if not swap:
            return


def main():
    input_file_pointer = open_file()
    file_contents = read_file(input_file_pointer)
    sort(file_contents)
    write_file(file_contents)

    # c1 = Card(3, 'D')
    # c2 = Card(3, 'D')
    # c1.is_bigger(c2.val, c2.suit)
    # print(c1.is_bigger(c2.val, c2.suit))


if __name__ == "__main__":
    main()
