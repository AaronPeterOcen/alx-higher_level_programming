#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    nm = dir(hidden_4)
    for nms in nm:
        if nms[:2] != "__":
            print(nms)
