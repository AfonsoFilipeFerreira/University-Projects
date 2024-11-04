from interface import interface


# Read the file that has the highest score
def load_highest_score():
    """
    Load the highest score from the 'highest_score.txt' file.

    Returns
    -------

    highest_score : int
        The highest score read from the file, or 0 if the file is not found (first run).
    """
    try:
        with open("highest_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        # If the file is not found (first run), return 0 as the default highest score
        return 0


highest_score = load_highest_score()


def main():
    """
    Entry point of the program.
    Initializes the highest score and launches the interface with the highest score.
    """
    interface(highest_score)


if __name__ == '__main__':
    main()
