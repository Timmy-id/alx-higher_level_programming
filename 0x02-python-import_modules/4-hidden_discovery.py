#!/usr/bin/python3
import importlib

if __name__ == "__main__":
    mod = importlib.import_module("hidden_4")
    content = dir(mod)
    for txts in content:
        if not txts.startswith("__"):
            print(txts)
