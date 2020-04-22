import os

def rename_files(src_path):
  """
  This function renames all the image files in the cleaned data folder
  """
  ctr = 0
  cleaned_data_folder_path = os.path.join(src_path[0:-4],"output","CLEANED_DATA")
  folders = os.listdir(cleaned_data_folder_path)
  for folder in folders:
    next_path = os.path.join(cleaned_data_folder_path,folder)
    contents = os.listdir(next_path)
    for img in contents:
      img_name = img.split("_")[0].strip(".jpg")
      new_name = img_name + "_" + str(ctr+100) + ".jpg"
      os.rename(os.path.join(next_path,img),os.path.join(next_path,new_name))
      ctr += 1

# rename_files("C:\\Users\\bidnu\\Documents\\Sem_6\\Deep_Learning_CIE\\Assignment_2-Completed\\output\\CLEANED_DATA")