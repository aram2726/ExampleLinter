from linter import ExampleLinter


linter = ExampleLinter()


if __name__ == "__main__":
    with open("example.code", "r") as file:
        for line in file.readlines():
            linter.check_end(line)
