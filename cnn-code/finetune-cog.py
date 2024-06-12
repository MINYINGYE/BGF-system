import os
import sys
import glob
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Input, Activation, Dropout, Flatten, Dense
from keras.applications.vgg16 import VGG16
from keras import optimizers
# from smallcnn import save_history

nb_epoch =200

result_dir = '/share_dir/add_hdd/newPaper/result/models'

if not os.path.exists(result_dir):
    os.mkdir(result_dir)

def save_history(history, result_file):
    loss = history.history['loss']
    accuracy = history.history['acc']
    val_loss = history.history['val_loss']
    val_accuracy = history.history['val_acc']
    nb_epoch = len(accuracy)

    with open(result_file, "w") as fp:
        fp.write("epoch\tloss\taccuracy\tval_loss\tval_accuracy\n")
        for i in range(nb_epoch):
            fp.write("%d\t%f\t%f\t%f\t%f\n" % (i, loss[i], accuracy[i], val_loss[i], val_accuracy[i]))

img_rows=128
img_cols=128
nb_val_samples=500 # check
batch_size=32
channels=3
nb_classes=500# check
samples_per_epoch=15078 # check

input_tensor = Input(shape=(img_rows, img_cols,3))
vgg16 = VGG16(include_top=False, weights='imagenet', input_tensor=input_tensor)

top_model = Sequential()
top_model.add(Flatten(input_shape=vgg16.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(nb_classes, activation='softmax'))

model = Model(input=vgg16.input, output=top_model(vgg16.output))

for layer in model.layers[:15]:
        layer.trainable = False

        model.compile(loss='categorical_crossentropy',
                      optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
                      metrics=['acc'])

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

path1="%s" % sys.argv[1]
path2="%s" % sys.argv[2]

test_datagen = ImageDataGenerator(rescale=1.0 / 255)
# check classes
classes = []
for f in glob.glob(path1+ "/*"):
   classes.append(os.path.basename(f))



train_generator = train_datagen.flow_from_directory(
    directory=path1,
    target_size=(img_rows, img_cols),
    color_mode='rgb',
    classes=classes,
    class_mode='categorical',
    batch_size=batch_size,
    shuffle=True)

test_generator = test_datagen.flow_from_directory(
    directory=path2,
    target_size=(img_rows, img_cols),
    color_mode='rgb',
    classes=classes,
    class_mode='categorical',
    batch_size=batch_size,
    shuffle=True)

history = model.fit_generator(
    train_generator,
    samples_per_epoch=samples_per_epoch,
    nb_epoch=nb_epoch,
    validation_data=test_generator,
    nb_val_samples=nb_val_samples)

model.save_weights(os.path.join(result_dir, 'cog.h5')) # check
save_history(history, os.path.join(result_dir, 'cog.txt')) # check

