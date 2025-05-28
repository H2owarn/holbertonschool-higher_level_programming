#!/usr/bin/env python3
"""This module create a class named VerboseList that extends the Python list class."""


class VerboseList(list):

    def append(self, items):
        """Add an item and print a notification."""

        super().append(items)
        print(f"Added [{items}] to the list.")

    def extend(self, items):
        """Extend the list and print a notification."""
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, items):
        """Remove an item and print a notification."""
        if items in self:
            super().remove(items)
            print(f"Removed [{items}] from the list.")
        else:
            print(f"Item [{items}] not found in the list.")


    def pop(self, index=-1):
        """Pop an item from the list and print a notification."""

        if index is None:
            items = super().pop()
        else:
            items = super().pop(index)

        print(f"Popped [{items}] from the list.")
        return items  # Return the removed item


