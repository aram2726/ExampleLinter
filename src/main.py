import sys

from linter import ExampleLinter


linter = ExampleLinter()

REQUIRED_ARGUMENTS_COUNT = 2


def main():
    """
    Main function of ExampleLinter.
    """
    arguments = sys.argv
    if len(arguments) < REQUIRED_ARGUMENTS_COUNT:
        print("Usage: \n python3 src/main.py <file_path>")
        return
    file_path = arguments[1]
    with open(file_path, "r") as file:
        for line in file.readlines():
            linter.check_end(line)


if __name__ == "__main__":
    main()