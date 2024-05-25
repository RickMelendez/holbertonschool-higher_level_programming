#!/usr/bin/env python3

class VerboseList(list):
    """
    Subclass of list that prints notifications
    when items are added or removed.
    """

    def append(self, item):
        """
        Adds an item and prints a notification.
        """
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, iterable):
        """
        Extends the list and prints a notification.
        """
        num_items = len(iterable)
        super().extend(iterable)
        print("Extended the list with {} items.".format(num_items))

    def remove(self, item):
        """
        Removes an item and prints a notification.
        """
        print("Removed {} from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Removes and prints a notification.
        """
        item = super().pop(index)
        print("Popped {} from the list.".format(item))
        return item
