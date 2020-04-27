# function calls the other modules and creates the required output files
import read_pdf_file as rd_file
import table_querry as tq
import rename_image_files as rename
import filter_images as filtimg
import datasplit
import folder_name_cleaning as clean
import os

if __name__ == "__main__":
  src_path = os.getcwd()
  rd_file.read_covert(src_path)
  df = tq.read_data(src_path)
  folder_names,loc = tq.get_needed_data(df)
  tq.create_cleaned_data(src_path,folder_names,loc)
  rename.rename_files(src_path)
  filtimg.keep_pic(src_path,"DWI")
  clean.rename_folders(src_path)
  clean.further_name_clean(src_path)
  datasplit.create_dataset(src_path)
  print("Successfully completed")

  rd_file.read_covert(src_path,True)
  inf_df = tq.read_data(src_path,True)
  inf_fold,inf_loc = tq.get_needed_data(inf_df,True)
  tq.create_cleaned_data(src_path,inf_fold,inf_loc,True)
  rename.rename_files(src_path,True)
  filtimg.keep_pic(src_path,"DWI",True)

  # 2 folders with almost same name so merging them manually here
  fold1 = "Right  parietal lobe"
  fold2 = "Right parietal lobe"
  base_path = os.path.join(src_path[0:-4],"output","Infer_data")
  clean.copyfile(os.path.join(base_path,fold1),os.path.join(base_path,fold2))
  os.rmdir(os.path.join(base_path,fold1))

  print("Successfully completed")