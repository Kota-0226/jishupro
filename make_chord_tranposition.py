"""
This file is used for transposing the chord progression.
"""



def chord_transpose(strings):
  #stringsはコードを想定。e.g. C#m,E-sus4
    if ("C#" in strings) or ("D-" in strings) :
        return 1
    elif ("D#" in strings) or ("E-" in strings):
        return 3
    elif ("F# "in strings) or ("G-" in strings) :
        return 6
    elif ("G#" in strings) or ( "A-" in strings):
        return 8
    elif ("A#" in strings) or ("B-" in strings):
        return 10
    elif "C" in strings:
        return 0
    elif "D" in strings:
        return 2
    elif "E" in strings:
        return 4
    elif "F" in strings:
        return 5
    elif "G" in strings:
        return 7
    elif "A" in strings :
        return 9
    else:
        return 11
