import sys
from matplotlib import pyplot
import keras
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os
import keras_to_tf as convmodel

# path = "C:/Users/bidnu/Documents/Sem_6/Deep_Learning_CIE/Assignment_2-Completed/output/CLEANED_DATA/"
src_path = os.getcwd()
path = os.path.join(src_path[0:-4],"output","CLEANED_DATA")
category_list = os.listdir(path)
op_layer = len(category_list) - 2
print(category_list)

training_data_dir = os.path.join(path,"train")
test_data_dir = os.path.join(path,"test")

# Added this so we know the class of images for testing to compare with prediction
test_img_ind = list()
test_folders = os.listdir(test_data_dir)
for i in range(len(test_folders)):
  if not (len(os.listdir(os.path.join(test_data_dir,test_folders[i]))) == 0):
    test_img_ind.append(i)

# define cnn model
def define_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer = 'he_uniform', padding='same',
                     input_shape=(200, 200, 3)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Dropout(0.3))

    model.add(Conv2D(16, (3, 3), activation='relu', kernel_initializer = 'he_uniform', padding='same'))
    model.add(MaxPooling2D((3, 3)))
    model.add(Dropout(0.1))

    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(op_layer, activation='softmax'))
    # compile model
    opt = SGD(lr=0.001, momentum=0.9)
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    return model


# plot diagnostic learning curves
def summarize_diagnostics(history):
    # plot loss
    pyplot.subplot(211)
    pyplot.title('Cross Entropy Loss')
    pyplot.plot(history.history['loss'], color='blue', label='train')
    # plot accuracy
    pyplot.subplot(212)
    pyplot.title('Classification Accuracy')
    pyplot.plot(history.history['accuracy'], color='blue', label='train')
    # save plot to file
    filename = sys.argv[0].split('/')[-1]
    pyplot.savefig(filename + '_plot.png')
    pyplot.close()


# run the test harness for evaluating a model
def run_test_harness():
    # define model
    model = define_model()
    # create data generator
    '''train_datagen = ImageDataGenerator(rescale=1.0 / 255.0,
                             rotation_range=90,
                             zoom_range=0.15,
                             width_shift_range=0.2,
                             height_shift_range=0.2,
                             shear_range=0.15,
                             horizontal_flip=True,
                             fill_mode="nearest")'''
    datagen = ImageDataGenerator(rescale=1.0 / 255.0)
    # prepare iterators
    train_it = datagen.flow_from_directory(training_data_dir,
                                           class_mode='categorical', batch_size=46, target_size=(200, 200),shuffle=False)
    test_it = datagen.flow_from_directory(test_data_dir,
                                          class_mode='categorical', batch_size=46, target_size=(200, 200),shuffle=False)
    # fit model
    history = model.fit_generator(train_it, steps_per_epoch=len(train_it), epochs=50, verbose=1)
    # evaluate model
    _, acc = model.evaluate_generator(test_it, steps=len(test_it), verbose=0)
    # k = model.predict(test_it)
    test_it.reset()
    k = model.predict_generator(test_it,steps=len(test_it),verbose=1)
    print(k)
    
    model.save("model.h5")
    print("Saved model to disk")
    
    #test_acc = history.history['test_acc']
    #print(test_acc)
    h = [np.argmax(x) for x in k]
    print(h)
    print(test_img_ind)
    s = 1
    for i in h:
        k = category_list[i]
        print('Test Image {}: Belongs to class {}'.format(s,k))
        s = s+1
    print('> %.9f' % (acc * 100.0))
    # learning curves
    summarize_diagnostics(history)


# entry point, run the test harness
run_test_harness()

# Convert the h5 model file to pb file
convmodel.main()
