# pip install tabula-py
# install java and add the bin folder to PATH variable
# using tabula modlule to convert table in pdf to csv file
from tabula import convert_into
import os
import shutil
import pandas as pd 

def read_covert(src_path,inference=False):
  """
  Reads the input pdf file and converts it to csv file
  """

  pdf_name = "ACUTE_INFARCTS_Updated.pdf"
  input_file_path = os.path.join(src_path[0:-4],"Assignment_2",pdf_name)

  if inference:
    pdf_name = "Inference_Data_GroundTruths.pdf"
    input_file_path = os.path.join(src_path[0:-4],"Inference_Data",pdf_name)

  output_dir_path = os.path.join(src_path[0:-4],"output")
  os.makedirs(output_dir_path,exist_ok=True)
  output_file_path = os.path.join(output_dir_path,pdf_name[0:-4]+".csv")  
  convert_into(input_file_path,output_file_path,output_format="csv",pages="all")