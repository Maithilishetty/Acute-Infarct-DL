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
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same',
                     input_shape=(200, 200, 3)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(46, activation='sigmoid'))
    # compile model
    opt = SGD(lr=0.001, momentum=0.9)
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
    datagen = ImageDataGenerator(rescale=1.0 / 255.0)
    # prepare iterators
    train_it = datagen.flow_from_directory(training_data_dir,
                                           class_mode='categorical', batch_size=64, target_size=(200, 200))
    test_it = datagen.flow_from_directory(test_data_dir,
                                          class_mode='categorical', batch_size=64, target_size=(200, 200))
    # fit model
    keras.callbacks.callbacks.EarlyStopping(monitor='train_acc', min_delta=0.1, patience=10, verbose=0, mode='auto',
                                            baseline=None, restore_best_weights=False)
    history = model.fit_generator(train_it, steps_per_epoch=len(train_it), epochs=50, verbose=1)
    # evaluate model
    _, acc = model.evaluate_generator(test_it, steps=len(test_it), verbose=0)
    k = model.predict(test_it)
    h = [np.argmax(x) for x in k]
    print(h)
    s = 1
    for i in h:
        k = category_list[i]
        print('Test Image {}: Belongs to class {}'.format(s,k))
        s = s+1
    #print('> %.9f' % (acc * 100.0))
    # learning curves
    summarize_diagnostics(history)


# entry point, run the test harness
run_test_harness()



