# -*- coding: utf-8 -*-
import sys

from trello.util import create_oauth_token


def main():
    try:
        command = sys.argv[1]
    except IndexError:
        return

    if command == "oauth":
        create_oauth_token()


if __name__ == "__main__":
    sys.exit(main())

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
