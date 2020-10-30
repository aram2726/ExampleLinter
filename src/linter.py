from typing import Tuple

from stack import Stack


class ExampleLinter:
    """
    Example linter for closing branckets.
    """

    symbol_pairs = {
        "(": ")",
        "{": "}",
        "[": "]",
    }

    def check_end(self, line: str) -> bool:
        """
        Check if line ends with `;` or not.
        :param line: Line in document.
        """
        print(line)
        line_result = self.match_symbols(line)
        if not line_result[0] and line_result[1].startswith("Unclosed"):
            print(line_result[1])
            print("==================================")
            return True
            # May be opening brackets like
            # {
            #   ...
            # }
        if line[-1] in self.symbol_pairs.values():
            print(line_result[1])
            print("==================================")
            return True  # No need to set semicolon after closing brackets.

        result = line.endswith(";")
        print(line_result[1])
        print("==================================")
        return result

    def match_symbols(self, line: str) -> Tuple[bool, str]:
        """
        Check if there are none closed brackets in line or senseless closing bracket.
        :param line: Line in document.
        :return: Boolena condition of line and a message.
        """
        openers = self.symbol_pairs.keys()
        closers = self.symbol_pairs.values()
        closing_items = []

        my_stack = Stack()

        index = 0
        while index < len(line):
            symbol = line[index]

            if symbol in openers:
                my_stack.push(symbol)
            else:  # The symbol is a closer.
                # If the stack is already empty, then symbols are not balanced.
                if my_stack.is_empty():
                    pass
                else:
                    # If there are still intems in Stack, check for a miss-match.
                    top_item = my_stack.peek()
                    if symbol == self.symbol_pairs[top_item]:
                        my_stack.pop()
                    else:
                        if symbol in closers:
                            closing_items.append(symbol)
            index += 1

        if closing_items:
            message = "Invalid closing `{}`.".format(", ".join(closing_items))
            print(message)
            return False, message

        if my_stack.is_empty():
            return True, "ok"

        message = "Unclosed `{}`.".format(", ".join(my_stack.items))
        print(message)
        return False, message
