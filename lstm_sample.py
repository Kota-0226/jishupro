from __future__ import print_function
#from tensorflow import keras
from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from keras.layers import LSTM
from keras.optimizers import RMSprop

import numpy as np
import random 
import sys
import io

from tqdm import tqdm
import music21 as m21
import os
import glob

#import classify_chordprogression as cc

DS = os.sep #これは"/"を意味する
bs = os.path.dirname(__file__) + DS #このファイルのありか
#xmlpath = bs + 'musicxml_simple'+ str(cc.result) + DS 
#model_weights_path = bs + 'melo_model' + str(cc.result) + 'w.hdf5'
#model_save_path = bs + 'melo_model' + str(cc.result) +'.hdf5'

xmlpath = bs + 'musicxml_simple8' + DS 
model_weights_path = bs + 'melo_model' + 'w.hdf5'
model_save_path = bs + 'melo_model'+'.hdf5'

make_model = False #後でもうすでに生成データがあるかの話

#music_keys = ('C', 'D', 'E', 'F', 'F#', 'G', 'A', 'B') 
music_keys = ('C')

#テキストの生成
text = []
#フォルダ内のxmlファイルを取得する

#note_txts = []
xmls = glob.glob(xmlpath + "*.mxl")

for x in tqdm(xmls):  
    #xmlを読み込む
    piece = m21.converter.parse(x)

#ここは移調を考える場合？
    for  trans_key in music_keys:
        k = piece.analyze('key')

        #主音を合わせる
        trans = trans_key

        i = m21.interval.Interval(k.tonic,m21.pitch.Pitch(trans))
        trans_piece = piece.transpose(i)
        ntxt = []
    #ntxt = []
        for n in piece.flat.notesAndRests:
            #n.name:音名の取得 n.duration.quaterLength:音の長さの取得(1拍,0.5拍など...)                    
            #ここは楽譜が単音だけ出ないとエラーを吐く                                                      
            text.append(str(n.name) + '_' + str(n.duration.quarterLength) + ' ')
            #count += float(n.duration.quarterLength)                                                      
            #print("n={}".format(n.duration.quarterLength))                                                
            #1曲が終わったら追加する                                                                               note_txts.append(' '.join(ntxt))

    #note_txts.append(' '.join(ntxt))

#text = '\n'.join(note_txts)


#ここからLSTM
print('---------start LSTM')
chars = text
count = 0
char_indices = {} #辞書
indices_char = {} #逆引き辞書
#print("xml_path={}".format(xmlpath))
#print("chars = {}".format(chars))



for word in chars:
    if not word in char_indices: #辞書になかったら
        char_indices[word] = count
        count += 1
        print(count,word) #登録した単語を表示,登録した単語の数も表示

#逆引き辞書を辞書から作成
indices_char = dict([(value,key) for (key,value) in char_indices.items()])

maxlen = 5
step = 1
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])

print('nb sequences:', len(sentences))

#モデルのファイルがある場合は読み取る
if(os.path.exists(model_save_path) and os.path.exists(model_weights_path)):
    print('-----------read Model')
    model=load_model(model_save_path)
    model.load_weights(model_weights_path)

else: #モデル生成準備
    make_model = True
    print('Vectorization...')
    x = np.zeros((len(sentences), maxlen, len(chars)), dtype=bool)
    y = np.zeros((len(sentences), len(chars)), dtype=bool)
    for i, sentence in enumerate(sentences):
        for t, char in enumerate(sentence):
            x[i, t, char_indices[char]] = 1
        y[i, char_indices[next_chars[i]]] = 1

    #モデル生成
    print('Build model...')
    model = Sequential()
    model.add(LSTM(500, input_shape=(maxlen, len(chars)),return_sequences=True))
    model.add(Dense(len(chars), activation='softmax'))

optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def on_epoch_end(epoch,_):
    print()
    print('---------Generating text after Epoch: %d' %epoch)
    start_index = random.randint(0,len(text) - maxlen - 1)
    start_index = 0 #テキストの最初からスタート
    for diversity in [0.2]: #ここは0.2のみ？
        print('-------diversity:',diversity)

        generated  =''
        sentence = text[start_index: start_index + maxlen]
        #sentenceはリストなので文字列に変換
        generated += ''.join(sentence)
        print(sentence)

        print('------Generateing with seed:"' + "".join(sentence) + '"')
        sys.stdout.write(generated)

        for i in range(100):
            x_pred = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x_pred[0, t, char_indices[char]] = 1.
            preds = model.predict(x_pred, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index]

            generated += next_char
            sentence = sentence[1:]
            sentence.append(next_char)

            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()
        
def on_train_end(logs):
    print('----- saving model.. ')
    model.save_weights(model_weights_path)
    model.save(model_save_path)

def make_melody(length=200):
    start_index = random.randint(0,len(text) - maxlen - 1)
    #start_index = 0 #テキストの最初からスタート

    print(start_index)
    for diversity in [0.2]: #ここは0.2のみ?
        print('--------diversity:', diversity)

        generated = ''
        sentence = text[start_index: start_index + maxlen]
        #sentenceはリストなので文字列へ変換
        generated += ''.join(sentence)
        print(sentence)

        print('--------- Generating with seed:"' + "".join(sentence) + '"')
        sys.stdout.write(generated)

        for i in range(length):
            #x_pred = np.zeros((1, maxlen, len(chars))) #len(chars)は183じゃなきゃいけないけど、なんか50だった。
            x_pred = np.zeros((1, maxlen, 183))
            for t, char in enumerate(sentence):
                x_pred[0, t, char_indices[char]] = 1.
            preds = model.predict(x_pred, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index]
                
            generated += next_char
            sentence = sentence[1:]
            sentence.append(next_char)

            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()

    return generated

if make_model:
    print_callback = LambdaCallback(on_epoch_end=on_epoch_end,on_train_end=on_train_end)
    model.fit(x,y,batch_size=128,epochs=120,callbacks=[print_callback])

print('---------print score')
melo_sentence = make_melody(20)
print("melo_sentence = {}".format(melo_sentence))

#メロディをmusicXMLに変換する

meas = m21.stream.Stream()
meas.append(m21.meter.TimeSignature('4/4'))
melo = melo_sentence.split()

for m in melo:
    print("melo={}".format(melo))
    ptch, dist = m.split('_')
    print("dist={}".format(dist))
    if(ptch == 'rest'):
        n = m21.note.Rest(quarterLength = float(dist))
    else:
        n = m21.note.Note(ptch,quarterLength = float(dist))

    meas.append(n)

    #print(note_dt)

meas.makeMeasures(inPlace=True)
meas.show('musicxml', addEndTimes=True)
