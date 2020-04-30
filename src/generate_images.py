from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import os
import numpy as np

# load the image
src_path = os.getcwd()
path = os.path.join(src_path[0:-4], "output", "CLEANED_DATA", "train")
folder_list = os.listdir(path)
folder_path = [os.path.join(path, i) for i in folder_list]
file_path = [os.path.join(i, j) for i in folder_path for j in os.listdir(i)]
img_folder_name = [i.split("\\")[-2] for i in file_path]
i = 0
count = 0
aug = ImageDataGenerator(
    rescale=1.0 / 255.0,
    zoom_range=0.15,
    shear_range=0.15,
    fill_mode="nearest")
# for subdir, dirs, files in os.walk(test_data_dir):
for subdir, dirs, files in os.walk(path):
    for filename in files:
        total = 0
        filepath = subdir + os.sep + filename
        print(subdir)
        print(filepath)
        image = load_img(filepath)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        imageGen = aug.flow(image, batch_size=1, save_to_dir=subdir, save_prefix="image", save_format="jpg")
        for image in imageGen:
                # increment our counter
            total += 1
                # if we have reached the specified number of examples, break
                # from the loop
            if total == 20:
                break
