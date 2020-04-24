
### Requirements:
1. Python 3.x
2. pandas, tabula-py, nltk, matplotlib, keras, numpy, tensorflow and opencv modules
   (can be install using "pip install module-name, module-name ...")
3. For tabula, JAVA needs to be installed and has to be added to the PATH variables in windows.
   To do this after installing JAVA, copy the path of the "bin" folder of the installation and add
   it to path variables by editing the system environment variables on the windows platform.

### Required Directories:
1. "Assignment_2" directory with all the case folders and patient information pdf file
2. "src" folder which has all the source codes (10 files)
   (Both these folders should be in the same directory like Desktop or Documents or any other folder)

Initial file sturcture:
Any folder (Documents or Desktop etc)  
&nbsp; &nbsp; |  
&nbsp; &nbsp; +-- dir Assignment_2 (folder with all case folders and pdf)  
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; |  
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- dir Case 1  
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- dir Case 2 ...  
&nbsp; &nbsp; |  
&nbsp; &nbsp; +-- dir src (folder with all source code)  
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; |  
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file main.py  
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file read_pdf_file.py  
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file table_querry.py  
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file renaming_image_files.py  
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file filter_images.py  
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file datasplit.py  
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file folder_name_cleaning.py  
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file cnn_model.py  
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file keras_to_tf.py  
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file inference_test.py  
&nbsp; &nbsp; |     
&nbsp; &nbsp; +-- file readme.txt
  

### Running the code:
1. Open the "src" folder
2. Open the file named as "main.py" and run it
3. Run "cnn_model.py" after "main.py"
4. Now use the Intel model_optimizer and generate xml and bin files for the model
5. Finally run "inference_test.py" for performing inference

### Output generated:
1. Creates a folder called "output"
2. This folder contains the csv file generated (ACUTE_INFARCTS_excel.csv) and used by the code and also
   another folder called "CLEANED_DATA"
3. "CLEANED_DATA" contains folders folders named as the location of the brain infarcts and each of
   these folders contains the brain images of the person who has an infarcts at that particular
   location
4. "CLEANED_DATA" also contains the "test" and "train" folders which has data used by the CNN model
5. In the "src" folder, the model files which are generated are saved

### CMD Commands:
1. To generate an XML and bin file: 

&nbsp; a. Run the setupvars.bat file to initialize the OpenVino Environment. 
&nbsp; b. Go to the model optimizer folder in IntelSWTools and run: python mo_tf.py --input_model <input_model_destination>.pb -b 1 --output_dir <output_directory> --scale 255 --data_type FP32

2. To obtain an inference on the input image: 

&nbsp; a. python inference_test.py -m <model_destination>.xml -i <input_image>
