# The following import allows using classes as type annotations in any order.
# Do not remove this as it fixes NameErrors in Python versions < 3.14.
"""
Custom Program Assignment: Wordy
"""

__author__ = "Kasra Asarroodi"

import wordy.utils as utils


def main():
    utils.display_title()
    utils.menu(utils.Statistics())


if __name__ == "__main__":
    main()