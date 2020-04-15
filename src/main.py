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
  datasplit.create_dataset(src_path)
  print("Successfully completed")