import inference_test2 as inf
import os
import glob

def choose_path(src_path,folder,inference=False):
  path = os.path.join(src_path[0:-4],"output","CLEANED_DATA",folder)
  if inference:
    path = os.path.join(src_path[0:-4],"output","Infer_data")
  return path

# path = os.path.join(src_path[0:-4],"output","CLEANED_DATA","train")
src_path = os.getcwd()
path = choose_path(src_path,"train")

folder_list = os.listdir(path)
folder_path = [os.path.join(path,i) for i in folder_list]
file_path = [os.path.join(i,j) for i in folder_path for j in os.listdir(i)]
img_folder_name = [i.split("\\")[-2] for i in file_path]

i=0
count = 0
# for subdir, dirs, files in os.walk(test_data_dir):
for subdir, dirs, files in os.walk(path):
  for filename in files:
    filepath = subdir + os.sep + filename
    if filepath.endswith(".jpg"):
      ind = inf.func(filepath,img_folder_name[i])
      if(ind):
        count = count + 1
      i=i+1
print('Accuracy is {} %'.format( (count/len(img_folder_name) )*100))
