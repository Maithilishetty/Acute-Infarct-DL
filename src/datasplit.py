import shutil #copy images to train, test and valid dirs
import os #files and dirs manipulation
import math #split calculate

def del_folder(cleaned_path):
  """
  Deletes the train and test folders if existing
  """
  data_set_dirs= ['train','test']
  for dsdirs in data_set_dirs:
    path = cleaned_path + '/'+ dsdirs
    if os.path.exists(path):
      shutil.rmtree(path)

def datasplit_init(cleaned_path):
  """
  Creates the train and test folders
  """
  #get category folder list
  os.chdir(cleaned_path)
  category_list = list(filter(lambda x: os.path.isdir(x), os.listdir()))

  #create training,validation,testing directories
  data_set_dirs= ['train','test']
  for dsdirs in data_set_dirs:
    path = cleaned_path + '/'+ dsdirs
    os.makedirs(path)

  # define proportion of data
  train_prop = 0.5
  test_prop = (1 - train_prop)
  return category_list,train_prop

# function to split data of each category into trainning, validation and testing set
def create_dataset(src_path):
  """
  Populates the train and test folders with the data
  """
  cleaned_path = os.path.join(src_path[0:-4],"output","CLEANED_DATA")
  del_folder(cleaned_path)
  category_list,train_prop = datasplit_init(cleaned_path)
  for ii, cat in enumerate(category_list):
    src_folder_path = cleaned_path + '/' + cat
    dest_dir1 = cleaned_path + '/train/' + cat
    dest_dir2 = cleaned_path + '/test/' + cat


    dest_dirs_list = [dest_dir1,dest_dir2]
    for dirs in dest_dirs_list:
      os.mkdir(dirs, 755)

    # get files' names list from respective directories
    os.chdir(src_folder_path)
    files = [f for f in os.listdir() if os.path.isfile(f)]

    # get training, testing and validation files count
    train_count = math.ceil(train_prop * len(files))
    test_count = int((len(files) - train_count))
    # get files to segregate for train,test and validation data set
    train_data_list = files[0: train_count]
    # print(train_data_list)
    test_data_list = files[train_count:train_count + 1 + test_count]
    # print(test_data_list)

    for train_data in train_data_list:
      train_path = src_folder_path + '/' + train_data
      shutil.copy(train_path, dest_dir1)

    for test_data in test_data_list:
      test_path = src_folder_path + '/' + test_data
      shutil.copy(test_path, dest_dir2)