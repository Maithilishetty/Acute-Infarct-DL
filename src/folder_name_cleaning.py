import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("stopwords")
nltk.download("punkt")

def name_cleaning(folder_path):
  """
  This function cleans the folder names
  """
  
  category_list = os.listdir(folder_path)

  stop_words = set(stopwords.words("English"))
  # splitting the folder names into words and making them lower case
  tokens = [word_tokenize(i) for i in category_list]
  # print(tokens[0:5])
  temp1 = list()
  for i in tokens:
    temp2 = [w.lower() for w in i]
    temp1.append(temp2)

  tokens = temp1

  # removing words like in,of,and,the etc
  cleaned_folders = list()
  for fold in tokens:
    words = [w for w in fold if not w in stop_words] 
    cleaned_folders.append(words)

  output_list = list()
  for i in cleaned_folders:
    fold = ""
    for j in i:
      fold = fold + j + "_"
    fold = fold[0:len(fold) - 1]
    output_list.append(fold)

  return output_list

def rename_folders(src_path):
  """
  This function renames the folders in train and test with the new folder names
  """
  cleaned_data_folder_path = os.path.join(src_path[0:-4],"output","CLEANED_DATA")
  # train_path = os.path.join(cleaned_data_folder_path,"train")
  # test_patth = os.path.join(cleaned_data_folder_path,"test")

  cleaned_folder_names = name_cleaning(cleaned_data_folder_path)
  # print(len(cleaned_folder_names))

  # folders = ["train","test"]
  # for folder in folders:
  # path = os.path.join(cleaned_data_folder_path,folder)
  folder_list = os.listdir(cleaned_data_folder_path)
  for i in range(len(folder_list)):
    os.rename(os.path.join(cleaned_data_folder_path,folder_list[i]),os.path.join(cleaned_data_folder_path,cleaned_folder_names[i]))

# rename_folders(os.getcwd())