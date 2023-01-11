#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    sort_scores = sorted(a_dictionary.items(), key=lambda x: x[1])[-1]
    dict_score = sort_scores[0]
    return dict_score
