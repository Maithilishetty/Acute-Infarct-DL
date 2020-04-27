import os

def rename_files(src_path,inference=False):
  """
  This function renames all the image files in the cleaned data folder
  """
  
  ctr = 0
  cleaned_data_folder_path = os.path.join(src_path[0:-4],"output","CLEANED_DATA")
  if inference:
    cleaned_data_folder_path = os.path.join(src_path[0:-4],"output","Infer_data")

  folders = os.listdir(cleaned_data_folder_path)
  for folder in folders:
    next_path = os.path.join(cleaned_data_folder_path,folder)
    contents = os.listdir(next_path)
    for img in contents:
      img_name = img[:-4]
      new_name = img_name + "_" + str(ctr+100) + ".jpg"
      if inference:
        new_name = img_name + "_" + "infer" + "_" + str(ctr+100) + ".jpg"
      os.rename(os.path.join(next_path,img),os.path.join(next_path,new_name))
      ctr += 1