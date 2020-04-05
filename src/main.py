# function calls the other modules and creates the required output files
import read_pdf_file as rd_file
import table_querry as tq
import rename_files as rename
import data_for_model as data
import os

if __name__ == "__main__":
  src_path = os.getcwd()
  rd_file.read_covert(src_path)
  df = tq.read_data(src_path)
  folder_names,loc = tq.get_needed_data(df)
  tq.create_cleaned_data(src_path,folder_names,loc)
  rename.rename_files(src_path)
  data.keep_pic(src_path,"DWI")
  print("Successfully completed")