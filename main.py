import music21 as m21
import os
import glob

import classify_chordprogression as cc
import make_melody as mm
import make_chords as mc

DS = os.sep #これは"/"を意味する                                                                                                                                        
bs = os.path.dirname(__file__) + DS #このファイルのありか                                                                                                               
xmlpath = bs + 'musicxml_simple' + str(cc.result) + DS

#print(type(xmlpath))
stream1 = mm.make_melody(xmlpath)

stream2 = m21.stream.Part()
        
l = len(cc.chord_progression)
for i in range(l):
    key = mc.chord_transpose(cc.chord_progression[i])
    if key > 5:
        key = -1 * (12 - key)
    n = mc.pickup_chordtype(cc.chord_progression[i]) #コードの種類が数字で返ってくる、詳しくはmake_chords.py参照
    chord = mc.return_chord_type(n) 
    stream2.append(chord.transpose(key))
    stream2.append(chord.transpose(key))

score = m21.stream.Score()

score.insert(0, stream1)
score.insert(0, stream2)


score.show('musicxml')


