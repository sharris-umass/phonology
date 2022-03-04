"""
Processes a letter or sequence of letters and returns IPA and environment
"""

import eng_to_ipa
# eng-to-ipa.get_rhymes("cheese")


class Letter2Phon:
    def __init__(self, word):
        self.word = word
        self.letters = [x.lower() for x in word]     # creates a list of letters
        self.ipa = eng_to_ipa.convert(word)         # holds IPA version of word

    def digraph(self, wordlist):
        """produce digraphs for the word, used for assessing phonetic environments"""
        digraphs = []
        i = 0
        while i < len(wordlist) - 1:
            dyad = wordlist[i] + wordlist[i + 1]
            digraphs.append(dyad)
            i = i + 1
        return digraphs

    def features(self, twofer):
        """Takes a digraph as a list of two, returns phon. features list of first letter"""

        def assign_feature(first, second):
            CON = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
                   'l', 'm', 'n', 'p', 'q', 'r', 's',
                   't', 'v', 'w', 'x', 'y', 'z', 'þ', 'ð', 'ƀ']
            VOW = ['a', 'e', 'i', 'o', 'u', 'æ', 'y']
            HIGH = ['i', 'o', 'y']
            LOW = ['æ', 'u', 'a']
            MID = ['e']
            NAS = ['n', 'm']
            LAT = ['l']
            ROUND = ['w', 'u', 'o']
            SPI = ['ƀ', 'ð', 'j', 'f', 'þ', 's']
            STO = ['b', 'd', 'g', 'p', 't', 'k']
            VOICED = ['b', 'd', 'g', 'ƀ', 'ð', 'j']
            UNVOICED = ['f', 'þ', 's', 'ƀ', 'ð', 'j']

            feature = []
            a, b = first, second
            if a in VOW:
                feature.append("VOW")
                if a in ROUND:
                    feature.append("+R")
                if a in HIGH:
                    feature.append("high")
                if a in LOW:
                    feature.append("low")
                if a in MID:
                    feature.append("mid")
                if b in NAS:
                    feature.append("+N")
                if b in VOICED:
                    feature.append("+V")
            if a in CON:
                feature.append("CON")
                if a in SPI:
                    feature.append("SPI")
                if a in STO:
                    feature.append("STOP")
                if a in VOICED:
                    feature.append("+V")
                if a in UNVOICED:
                    feature.append("-V")
                if a in ROUND:
                    feature.append("+R")
            if a in NAS:
                feature.append("+N")
            if a in LAT:
                feature.append("LAT")
            return feature

        return assign_feature(twofer[0], twofer[1])


# TODO: How to process last letter of word? If taking two values raises an error, escape to process last letter.
