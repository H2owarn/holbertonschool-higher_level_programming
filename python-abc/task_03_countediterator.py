#!/usr/bin/env python3
"""This module Create a class named CountedIterator that extends
 the built-in iterator obtained from the iter function."""

class CountedIterator:
    def __init__(self, iterable):
        """Initialize iterator and counter."""

        self.iterator = iter(iterable)   # Get built-in iterator
        self.count = 0   # Track number

    def __iter__(self):
        return self

    def __next__(self):
        """Retrieve the next item and update the count.Raises StopIteration automatically."""

        try:
            item = next(self.iterator)
            self.count += 1

            return item

        except StopIteration:
            raise StopIteration  # Explicitly raise if iteration is done

    def get_count(self):
        """Return the current count of iterated items."""
        return self.count
