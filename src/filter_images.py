import os

def keep_pic(src_path,pic_name,inference=False):
  """
  This function chooses the required pics from cleaned data and deletes the other pics.
  """
  
  cleaned_data_folder_path = os.path.join(src_path[0:-4],"output","CLEANED_DATA")
  if inference:
    cleaned_data_folder_path = os.path.join(src_path[0:-4],"output","Infer_data")

  folders = [i for i in os.listdir(cleaned_data_folder_path) if os.path.isdir(os.path.join(cleaned_data_folder_path,i))]
  for folder in folders:
    folder_path = os.path.join(cleaned_data_folder_path,folder)
    files = os.listdir(folder_path)
    for img in files:
      if pic_name not in img:
        os.remove(os.path.join(folder_path,img))
      if "resz" in img:
        os.remove(os.path.join(folder_path,img))
      else:
        pass