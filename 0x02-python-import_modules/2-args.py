#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lists = len(sys.argv) - 1
    if lists == 0:
        print("0 arguments.")
    elif lists == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(lists))
    for i in range(lists):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
