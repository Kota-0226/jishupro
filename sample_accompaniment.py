import music21 as m21
import os
import glob

import make_chords as mc

#DS = os.sep #これは"/"を意味する                                                                          
#bs = os.path.dirname(__file__) + DS #このファイルのありか                                                 
#xmlpath = bs + 'sample_folder' + DS


stream1 = m21.stream.Part()
stream1.append(m21.meter.TimeSignature('4/4'))
meas = "rest_0.5 G_0.25 F_0.25 F_0.5 E_0.25 D_0.25 E_1.0 rest_0.5 C_0.25 D_0.25"
melo = meas.split()
for m in melo: #[E_0.5,E_0.5,D_0.5,C#_0.5,...]のデータを順に処理
    ptch,dist = m.split('_') #アンダーバーで区切る                                                               
    if(ptch == 'rest'): #rest=休符,この場合は休符の長さだけ追加                                                   
        n = m21.note.Rest(quarterLength = float(dist))
    else: #音と音符の長さを追加                                                                                   
        n = m21.note.Note(ptch,quarterLength = float(dist))
        #楽譜に追加                                                                                                
    stream1.append(n)





cMinor = m21.chord.Chord(["c3","g3","e-3"])
rest1 = m21.note.Rest()
rest1.quarterLength = 0.5
noteASharp = m21.note.Note('A#3')
noteASharp.quarterLength = 1.5


print("please input chord")
chord_progression = input().split()



def return_chord_type(n):
    if n==1:
        return mc.minor
    elif n==2:
        return mc.dim
    elif n==3:
        return mc.aug
    elif n==4:
        return mc.maj7
    elif n==5:
        return mc.min7
    elif n==6:
        return mc.seventh
    elif n==7:
        return mc.dim7
    elif n==8:
        return mc.hdim7
    elif n==9:
        return mc.minmaj7
    elif n==10:
        return mc.maj6
    elif n==11:
        return mc.min6
    elif n==12:
        return mc.ninth
    elif n==13:
        return mc.maj9
    elif n==14:
        return mc.min9
    elif n==15:
        return mc.sus2
    elif n==16:
        return mc.sus4
    else:
        return mc.major

stream2 = m21.stream.Part()
        
l = len(chord_progression)
for i in range(l):
    key = mc.chord_transpose(chord_progression[i])
    if key > 5:
        key = -1 * (12 - key)
    n = mc.pickup_chordtype(chord_progression[i]) #コードの種類が数字で返ってくる、詳しくはmake_chords.py参照
    chord = return_chord_type(n) 
    stream2.append(chord.transpose(key))
    stream2.append(chord.transpose(key))
    
    





score = m21.stream.Score()

score.insert(0, stream1)
score.insert(0, stream2)


score.show('musicxml')

"""
meas1 = m21.stream.Part()
meas2 = m21.stream.Part()

meas1.append(m21.meter.TimeSignature('4/4')) #拍子を4/4で固定
meas2.append(m21.meter.TimeSignature('4/4')) #拍子を4/4で固定
"""
