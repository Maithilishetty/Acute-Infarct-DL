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

  # further cleaning manually by hardcoding
  folder_list_to_merge2 = [["lacunar_infarct_dorsal_aspect_pons","dorsal_aspect_pons"],
  ["lacunar_infarct_medulla_oblongata_left","medulla_oblongata_left"],
  ["lacunar_infarct_pons_left","pons_left"],
  ["lacunar_infarct_posterior_limb_left_internalcapsule","posterior_limb_left_internalcapsule"],
  ["lacunar_infarct_right_putamen","right_putamen"],
  ["lacunar_infarcts_left_corona_radiata","left_corona_radiata"]]

  for i in folder_list_to_merge2:
    os.rename(i[0],i[-1])

  folder_list = os.listdir(cleaned_data_folder_path)
  for fold in folder_list:
    if len(os.listdir(fold)) == 0:
      os.rmdir(fold)