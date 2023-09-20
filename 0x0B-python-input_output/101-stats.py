#!/usr/bin/python3

"""
Module: 101-stats
Reads from standard input and computes metrics.
"""


def print_stats(size, codes_status):
    """
    Print accumulated metrics.
    Args:
        size (int): Accumulated read file size.
        codes_status (dict): Accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(codes_status):
        print("{}: {}".format(key, codes_status[key]))


if __name__ == "__main__":
    import sys

    size = 0
    codes_status = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, codes_status)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if codes_status.get(line[-2], -1) == -1:
                        codes_status[line[-2]] = 1
                    else:
                        codes_status[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, codes_status)

    except KeyboardInterrupt:
        print_stats(size, codes_status)
        raise
