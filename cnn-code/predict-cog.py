# coding:utf-8
import os
import sys
from keras.applications.vgg16 import VGG16
from keras.models import Sequential, Model
from keras.layers import Input, Activation, Dropout, Flatten, Dense
from keras.preprocessing import image
import numpy as np
import glob
import time
from tqdm import tqdm

# if len(sys.argv) != 2:
# print("usage: python predict.py [filename]")
# sys.exit(1)

filename = sys.argv[1]
path3 = sys.argv[2]

result_dir = '/share_dir/add_hdd/newPaper/result/models'
path2 = '/share_dir/add_hdd/newPaper/result/divid-test/divid0115-test/'
classes = []
for f in glob.glob(path2 + "/*"):
    classes.append(os.path.basename(f))
# print(classes)
nb_classes = len(classes)
# print(nb_classes)

img_height, img_width = 128, 128  # 縦, 横 ここを間違えるととんでもない分類結果になる
channels = 3

# VGG16
input_tensor = Input(shape=(img_height, img_width, channels))
vgg16 = VGG16(include_top=False, weights='imagenet', input_tensor=input_tensor)

# FC
fc = Sequential()
fc.add(Flatten(input_shape=vgg16.output_shape[1:]))
fc.add(Dense(256, activation='relu'))
fc.add(Dropout(0.5))
fc.add(Dense(nb_classes, activation='softmax'))

fc.summary()
# VGG16とFCを接続
model = Model(inputs=vgg16.input, outputs=fc(vgg16.output))


# model.summary()

# 学習済みの重みをロード
model.load_weights(os.path.join(result_dir, 'cog.h5'))  # check

#print("finisheddddd")

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
# model.summary()
last = []
# print('input:', filename)
for FN in tqdm(glob.glob(filename + "/*")):
    # time.sleep(0.01)
    read_name = FN.split('/', 2)[2]
    # print(read_name)
    # 画像を読み込んで4次元テンソルへ変換
    img = image.load_img(FN, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    # 学習時にImageDataGeneratorのrescaleで正規化したので同じ処理が必要！
    # これを忘れると結果がおかしくなるので注意
    x = x / 255.0

    # print(x)
    # print(x.shape)

    # クラスを予測
    # 入力は1枚の画像なので[0]のみ
    pred = model.predict(x)[0]
    # 予測確率が高いトップ5を出力
    top = 1
    top_indices = pred.argsort()[-top:][::-1]
    # print(top_indices)
    #result = [(classes[i], read_name) for i in top_indices]
    # hitotsu = []
    #for x in result:
        #last.append(x)
    result = [classes[top_indices[0]], read_name]
    # print(result)
    last.append(result)
last_array = np.array(last)
# print(last_array)
# np.savetxt(path3, last_array, fmt='%s %s', delimiter="\n")
np.save(path3, last_array)

