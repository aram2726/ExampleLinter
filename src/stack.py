from typing import Optional


class Stack:
    """
    Stack data structure implementation.
    """

    def __init__(self):
        self.items = []

    def push(self, item) -> None:
        """
        Accepts an item as a parameter and appends it to the end of the list.
        The runtime of this method is O(1) or constant time, 
        becasus appending to the end of list happenes in a constant time.
        """
        self.items.append(item)

    def pop(self) -> None:
        """
        Removes and returns the last item for the list, which is also the top of the Stack.
        """
        return self.items.pop() if not self.is_empty() else None

    def peek(self) -> Optional[str]:
        """
        This method returns the last item in the list, which is also item at the top of the Stack.
        """
        return self.items[-1] if not self.is_empty() else None

    def size(self) -> int:
        """
        This method returns the length of the list that is representing the Stack.
        """
        return len(self.items)

    def is_empty(self) -> bool:
        """
        This method returns a boolean value describing whether or not the Stack is empty.
        """
        return not self.items
