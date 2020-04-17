import sys
from matplotlib import pyplot
import keras
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os

path = "D:/Academics/ECE/Sem 6/DeepLearning/Project/output/CLEANED_DATA/"
category_list = os.listdir(path)
print(category_list)

training_data_dir = path + "train"
test_data_dir = path + "test"

# define cnn model
def define_model():
    model = Sequential()
    model.add(Conv2D(32, (5, 5), activation='relu', kernel_initializer='he_uniform', padding='same',
                     input_shape=(200, 200, 3)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='random_uniform', padding='same'))
                     #input_shape=(200, 200, 3)))
    model.add(MaxPooling2D((4, 4)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(46, activation='softmax'))
    # compile model
    opt = SGD(lr=0.001, momentum=0.8)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
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
    #datagen = ImageDataGenerator(rescale=1.0 / 255.0)#, horizontal_flip=True,zoom_range=[0.5,1.0])
    # prepare iterators
    train_datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    output = r"D:\Academics\ECE\Sem 6\DeepLearning\Project\output\CLEANED_DATA\example"
    train_it = train_datagen.flow_from_directory(training_data_dir,
                                           class_mode='categorical', batch_size=46, target_size=(200, 200), save_to_dir= output, save_prefix='image', save_format='jpg')
    test_it = test_datagen.flow_from_directory(test_data_dir,
                                          class_mode='categorical', batch_size=46, target_size=(200, 200))
    # fit model
    keras.callbacks.callbacks.EarlyStopping(monitor='train_acc', min_delta=0.1, patience=10, verbose=1, mode='auto',
                                            baseline=0.6, restore_best_weights=True)
    history = model.fit_generator(train_it, steps_per_epoch=1, epochs=40, verbose=1)
    # evaluate model
    _, acc = model.evaluate_generator(test_it, steps=len(test_it), verbose=0)
    k = model.predict(test_it)

    model.save("model.h5")
    print("Saved model to disk")
    
    h = [np.argmax(x) for x in k]
    print(h)
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
