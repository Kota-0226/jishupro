import music21 as m21
import numpy as np

#strings にはコード進行が入るつもり
def pickup_chordtype(strings):
    if len(strings) == 1:
        return 0
    elif (strings[1] == "#") or (strings[1] == "-"):
        return chordtype(strings[2:])
    else:
        return chordtype(strings[1:])



def chordtype(s):
    if s == "m":
        return 1
    elif s == "dim":
        return 2
    elif s == "aug":
        return 3
    elif s == "M7":
        return 4
    elif s == "m7":
        return 5
    elif s == "7":
        return 6
    elif s == "dim7":
        return 7
    elif s == "hdim7":
        return 8
    elif s == "mM7":
        return 9
    elif s == "M6":
        return 10
    elif s == "m6":
        return 11
    elif s == "9":
        return 12
    elif s == "M9":
        return 13
    elif s == "m9":
        return 14
    elif s == "sus2":
        return 15
    elif s == "sus4":
        return 16
    else: #とりあえずどこにも当てはまらないやつが入力されたら、基本のmajorスケールのコードとして返す。
        print("This chord ({}) isn't expected to be entered,so we regard {} as major chord.".format(s,s))
        return 0
