#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    my_list = [x for x in sentence]
    return (len("".join(my_list)), my_list[0])
