#!/usr/bin/python3
def magic_string(like_static: dict = {"count": 0}) -> str:
    like_static["count"] += 1
    return f"Holberton, " * like_static["count"][:-2]
