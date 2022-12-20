import music21 as m21
import os
import glob

import classify_chordprogression as cc
import make_melody as mm

DS = os.sep #これは"/"を意味する                                                                                                                                        
bs = os.path.dirname(__file__) + DS #このファイルのありか                                                                                                               
xmlpath = bs + 'musicxml_simple' + str(cc.result) + DS

#print(type(xmlpath))
mm.make_melody(xmlpath)

