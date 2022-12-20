import music21 as m21
import numpy as np

import make_chord_tranposition as mct
import pickup_chordtype as pc

"""
a0 = major
a1 = minor
a2 = dim
a3 = aug
a4 = maj7
a5 = min7
a6 = seventh
a7 = dim7
a8 = hdim7
a9 = minmaj7
a10 = maj6
a11 = min6
a12 = ninth
a13 = maj9
a14 = min9
a15 = sus2
a16 = sus4
"""
major = m21.chord.Chord(['c','e','g'])
minor = m21.chord.Chord(['c','e-','g'])
dim = m21.chord.Chord(['c','e-','g-'])
aug = m21.chord.Chord(['c','e','g#'])
maj7 = m21.chord.Chord(['c','e','g','b'])
min7 = m21.chord.Chord(['c','e-','g','b-'])
seventh = m21.chord.Chord(['c','e','g','b-'])
dim7 = m21.chord.Chord(['c','e-','g-','a']) 
hdim7 = m21.chord.Chord(['c','e-','g-','a#'])
minmaj7 = m21.chord.Chord(['c','e-','g','b'])
maj6 = m21.chord.Chord(['c','e','g','a'])
min6 = m21.chord.Chord(['c','e-','g','a'])
ninth = m21.chord.Chord(['c','d','e','g','b-'])
maj9 = m21.chord.Chord(['c','d','e-','g','b'])
min9 = m21.chord.Chord(['c','d','e-','g','b-'])
sus2 = m21.chord.Chord(['c','d','g'])
sus4 = m21.chord.Chord(['c','f','g'])

a = np.zeros((17,12),dtype = int)
a[0] = np.array([1,0,0,0,1,0,0,1,0,0,0,0])
a[1] = np.array([1,0,0,1,0,0,0,1,0,0,0,0])
a[2] = np.array([1,0,0,1,0,0,1,0,0,0,0,0])
a[3] = np.array([1,0,0,0,1,0,0,0,1,0,0,0])
a[4] = np.array([1,0,0,0,1,0,0,1,0,0,0,1])
a[5] = np.array([1,0,0,1,0,0,0,1,0,0,1,0])
a[6] = np.array([1,0,0,0,1,0,0,1,0,0,1,0])
a[7] = np.array([1,0,0,1,0,0,1,0,0,1,0,0])
a[8] = np.array([1,0,0,1,0,0,1,0,0,0,1,0])
a[9] = np.array([1,0,0,1,0,0,0,1,0,0,0,1])
a[10] = np.array([1,0,0,0,1,0,0,1,0,1,0,0])
a[11] = np.array([1,0,0,1,0,0,0,1,0,1,0,0])
a[12]= np.array([1,0,1,0,1,0,0,1,0,0,1,0])
a[13] = np.array([1,0,1,0,1,0,0,1,0,0,0,1])
a[14] = np.array([1,0,1,1,0,0,0,1,0,0,1,0])
a[15] = np.array([1,0,1,0,0,0,0,1,0,0,0,0])
a[16] = np.array([1,0,0,0,0,1,0,1,0,0,0,0])

chord_key = ["C","C#","C-","D","D#","D-","E","E#","E-","F","F#","F-","G","G#","G-","A","A#","A-","B","B#","B-",]

"""
print("Just enter 8 chords and it will automatically generate a melody in 4/4 time for 4 measures.")
print("Enter eight chord progressions that form the base of the melody, separated by one-byte spaces. Each chord is equivalent to two beats.")
print("In addition, the following chords can be used.")
print("maj,min,dim,aug,M7,m7,7,dim7,hdim7,mM7,M6,m6,9,M9,m9,sus2,sus4")
print("when you enter the chord progression,please following the following rules.")
print("1.Enter '-' for flat (♭)")
print("2.If you want to enter 'C major',please enter 'C'")
print("3.In other case,please enter 'RootNote + Chordname' e.g. 'C major 7' -> 'CM7'")
print("Example: C C-sus2 E#m Em Am Am Dm Dm")
print(" ")
print("Please input chords progression.")
chord_progression = input().split()
print(chord_progression)


transpose = [0 for i in range(8)]
chord_type = [0 for i in range(8)]
count = 0
for chord in chord_progression:
    transpose[count] = mct.chord_transpose(chord) #コード進行のベース音が入る
    chord_type[count] = pc.pickup_chordtype(chord) #コード進行の種類が入る
    count += 1
    
print(transpose)
print(chord_type)
"""


