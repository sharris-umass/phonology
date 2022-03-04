#! usr/bin/env python3

import grapheme


def write_rule(rule):
    pass


def read_rule(feature):
    pass


def check_sequence(r1, r2):
    pass


if __name__ == '__main__':
    input_word = input("Word? ")
    word = grapheme.Letter2Phon(input_word)
    these_letters = word.letters
    this_ipa = word.ipa
    these_digraphs = word.digraph(these_letters)
    these_features = [word.features(x) for x in these_digraphs]

    # last digraph
    _, last_letter = these_digraphs[-1]
    last_pair = word.features(last_letter + last_letter)
    these_features.append(last_pair)

    print(f"\tLetters: {these_letters}")
    print(f"\tDigraphs: {these_digraphs}")
    if "*" in word.ipa:
        print(f"\tIPA unavailable for {this_ipa}")
    else:
        print(f"\tIPA: {this_ipa}")

    print(f"Features: {these_features}")