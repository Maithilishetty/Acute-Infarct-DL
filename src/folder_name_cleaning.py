import os
import nltk
import glob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk.download("stopwords")
# nltk.download("punkt")

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

  cleaned_folder_names = name_cleaning(cleaned_data_folder_path)

  folder_list = os.listdir(cleaned_data_folder_path)
  for i in range(len(folder_list)):
    os.rename(os.path.join(cleaned_data_folder_path,folder_list[i]),os.path.join(cleaned_data_folder_path,cleaned_folder_names[i]))

# rename_folders(os.getcwd())
def copyfile(src_path,dest_path):
  files = [f for f in os.listdir(src_path) if f.endswith('.jpg')]
  sfolder_path = os.path.abspath(src_path)
  dfolder_path = os.path.abspath(dest_path)
  for f in files:
    os.rename(os.path.join(sfolder_path,f),os.path.join(dfolder_path,f))

def further_name_clean(src_path):
  cleaned_data_folder_path = os.path.join(src_path[0:-4],"output","CLEANED_DATA")
  os.chdir(cleaned_data_folder_path)
  
  folder_list_to_merge = [["lacunar_infarct_left_parietal_lobe","left_parietal_lobe"],
  ["lacunar_infarct_right_corona_radiata","right_corona_radiata"],
  ["lacunar_infarcts_bilateral_occipital_lobes","bilateral_occipital_lobes"],
  ["lacunar_infarcts_right_parietal_lobe","right_parietal_lobe"],
  ["left_cerebellar_lacunar_infarcts","left_cerebellar_hemisphere"],
  ["right_cerebellar_hemisphere_infarct","right_cerebellar_hemisphere"],
  ["right_parietal_lacunar_infarct","right_parietal_lobe"]]

  for i in folder_list_to_merge:
    copyfile(i[0],i[-1])

  folder_list = os.listdir(cleaned_data_folder_path)
  for fold in folder_list:
    if len(os.listdir(fold)) == 0: # Check is empty..
      os.rmdir(fold) # Delete..


# def further_name_clean1(src_path):
#   cleaned_data_folder_path = os.path.join(src_path[0:-4],"output","CLEANED_DATA")
#   os.chdir(cleaned_data_folder_path)
#   # os.makedirs("temp",exist_ok=True)
#   folder_list = os.listdir(cleaned_data_folder_path)
#   folder_list = [f.split("_") for f in folder_list]
#   # print(folder_list)
#   word_list = ["lacunar","infarcts","infarct","lobe"]

#   new_folder_list = list()
#   for fold in folder_list:
#     temp = [w for w in fold if not w in word_list]
#     new_folder_list.append(temp)
#   # print(new_folder_list)

#   temp1 = []
#   for i in new_folder_list:
#     temp2 = "" 
#     for j in i:
#       temp2 = temp2 + j + "_"
#     # print(temp2)
#     temp1.append(temp2[0:-1])

#   print(temp1)

#   # for i in temp1:
#   #   # print(i)
#   #   # print(type(i))
#   #   if not os.path.exists(i):
#   #     print("here")
#   #     os.makedirs(i)

#   # print(temp1)
#   duplicates = set([x for x in temp1 if temp1.count(x) > 1])
#   print(duplicates)
  
#   # idx = list()
#   # for i in duplicates:
#   #   indices = [j for j,x in enumerate(temp1) if i in x]
#   #   print(i)
#   #   print(indices)
#   #   for k in indices[1:]:
#   #     print(k)
#   #     print(temp1[k])
#   #     copyfile(temp1[k],i)
#     # idx.extend(indices)
#     # if i in temp1:
#       # ind = temp1.index(i)
#       # print(ind)
#   #     copyfile(temp1[ind],i)
#   #   else:
#   #     pass
#     # old_folder1 = "lacunar_infarct_" + i
#     # old_folder2 = "lacunar_infarcts_" + i
#     # old_folder3 = i + "_lacunar_infarcts"
#     # old_folder4 = i + "_lacunar_infarct"
#     # old_folder5 = i + "_infarcts"
#     # old_folder6 = i + "_infarct"
#     # old_folder7 = i + "_lobe"
#     # print(old_folder1)
#     # print(i)
#     # if os.path.exists(old_folder1):
#     #   copyfile(old_folder1,i)
#     # elif os.path.exists(old_folder2):
#     #   copyfile(old_folder2,i)
#     # elif os.path.exists(old_folder3):
#     #   copyfile(old_folder3,i)
#     # elif os.path.exists(old_folder4):
#     #   copyfile(old_folder4,i)
#     # elif os.path.exists(old_folder5):
#     #   copyfile(old_folder5,i)
#     # elif os.path.exists(old_folder6):
#     #   copyfile(old_folder6,i)
#     # elif os.path.exists(old_folder7):
#     #   copyfile(old_folder7,i)
#     # else:
#     #   pass

#   # folder_list = os.listdir(cleaned_data_folder_path)
#   # for fold in folder_list:
#   #   if len(os.listdir(fold)) == 0: # Check is empty..
#   #     os.rmdir(fold) # Delete..

# further_name_clean(os.getcwd())