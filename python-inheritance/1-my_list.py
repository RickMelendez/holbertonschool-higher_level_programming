#!/usr/bin/python3
"""MyList
"""


class MyList(list):
    """A list
    """

    def print_sorted(self):
        """Prints self in sorted format
        """

        print(sorted(self))
