import inference_test2 as inf
import os
import glob
#i = 0
src_path = os.getcwd()
path = os.path.join(src_path[0:-4],"output","CLEANED_DATA")

test_data_dir = os.path.join(path,"train")

test_img_ind = list()
test_folders = os.listdir(test_data_dir)
x = 0
for subdir, dirs, files in os.walk(test_data_dir):

    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".jpg"):
            test_img_ind.append((x-1))
    x = x + 1
'''for i in range(len(test_folders)):
  if not (len(os.listdir(os.path.join(test_data_dir,test_folders[i]))) == 0):
    test_img_ind.append(i)'''
#for filepath in glob.iglob(r'C:\Users\Anish\Desktop\Test_Images\*.jpg'):
#    inf.func(filepath)
print(test_img_ind)
i=0
count = 0
for subdir, dirs, files in os.walk(test_data_dir):
    for filename in files:
        filepath = subdir + os.sep + filename

        if filepath.endswith(".jpg"):
            ind = inf.func(filepath,test_img_ind[i])
            if(ind):
                count = count + 1
            i=i+1
print('Accuracy is {} %'.format( (count/len(test_img_ind) )*100))
