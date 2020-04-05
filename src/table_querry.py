import pandas as pd 
import os
import shutil

import read_pdf_file

def read_data(src_path):
  """
  Input is the path of the running script\n
  Reads the csv file created and return the dataframe\n
  """
  data_frame_path = os.path.join(src_path[0:-4],"output","ACUTE_INFARCTS_excel.csv")
  df = pd.read_csv(data_frame_path)
  df.columns = df.columns.str.strip()
  df = df.sort_values(df.columns[-1])
  return df

def get_needed_data(df):
  """
  Input is the dataframe\n
  Processes the dataframe and returns the list of patient names and location of infarcts
  """
  name_loc = df[["Name",df.columns[-1]]]
  names = name_loc["Name"].to_list()
  loc = name_loc["Location of acute infarct"].to_list()
  loc = [i.replace("\r","") for i in loc]
  folder_names = ["Case " + i[1:] for i in names]
  return folder_names,loc


def create_cleaned_data(src_path,folder_names,loc):
  """
  Input is source path, folder names and location of infarcts\n
  Creates new folder for cleaned data which contains folders for all locations of infarcts\n
  Copies appropriate case folder images to their relevant dest folder
  """
  cleaned_data_folder_path = os.path.join(src_path[0:-4],"output","CLEANED_DATA")
  if os.path.exists(cleaned_data_folder_path):
    shutil.rmtree(cleaned_data_folder_path)
    os.makedirs(cleaned_data_folder_path)
  else:
    os.makedirs(cleaned_data_folder_path)
  casefolder_base_path = os.path.join(src_path[0:-4],"Assignment_2")

  for i in range(len(folder_names)):
    case_folder_path = os.path.join(casefolder_base_path,folder_names[i])
    images_in_case_folder = os.listdir(case_folder_path)
    dest_path = os.path.join(cleaned_data_folder_path,loc[i])
    os.makedirs(dest_path,exist_ok=True)
  
    for img in images_in_case_folder:
      img_path = os.path.join(case_folder_path,img)
      img_name = img[0:-4]
      dest_img_path = os.path.join(dest_path,img)

      if (os.path.exists(dest_img_path)==False):
        shutil.copy(img_path,dest_path)
      elif os.path.exists(dest_img_path):
        num = 1
        while os.path.exists(dest_img_path[0:-4] + "_" + str(num) + ".jpg"):
          num += 1
        new_name = img_name + "_" + str(num) + ".jpg"
        new_img_path = os.path.join(dest_path,new_name)
        shutil.copy(img_path, new_img_path)