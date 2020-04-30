
### Requirements:
1. Python 3.x </br>
2. Tensorflow 1.15 </br>
3. pandas, tabula-py, nltk, matplotlib, keras, numpy, tensorflow and opencv modules
(can be install using "pip install <module_name>, <module_name> ...") </br>
4. For tabula, JAVA needs to be installed and has to be added to the PATH variables in windows. </br>
To do this after installing JAVA, copy the path of the "bin" folder of the installation and add it to path variables by editing the system environment variables on the windows platform. </br>

### Required Directories:
1. "Assignment_2" directory with all the case folders and patient information pdf file </br>
2. "src" folder which has all the source codes (12 .py files) </br>
   (Both these folders should be in the same directory like Desktop or Documents or any other folder) </br>

Initial file sturcture: </br>
Any folder (Documents or Desktop etc) </br>
&nbsp; &nbsp; | </br>
&nbsp; &nbsp; +-- dir Assignment_2 (folder with all case folders and pdf) </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; | </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- dir Case 1 </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- dir Case 2 ... </br>
&nbsp; &nbsp; | </br>
&nbsp; &nbsp; +-- dir Inference_Data (folder with inference data) </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; | </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- dir Case 1 </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- dir Case 2 ... </br>
&nbsp; &nbsp; | </br>
&nbsp; &nbsp; +-- dir src (folder with all source code) </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; | </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file main.py </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file read_pdf_file.py </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file table_querry.py </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file renaming_image_files.py </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file filter_images.py </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file datasplit.py </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file folder_name_cleaning.py </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file cnn_model.py </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file keras_to_tf.py </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file inference_test2.py </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file inference_test.py </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file final.py </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file generate_images.py </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file model.h5 </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file model.h5.pb </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file model.h5.xml </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file model.h5.bin </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file model.h5.mapping </br>
&nbsp; &nbsp; |&nbsp; &nbsp; &nbsp; &nbsp; +-- file cnn_model.py_plot.png </br>
&nbsp; &nbsp; | </br>
&nbsp; &nbsp; +-- file readme.md </br>
&nbsp; &nbsp; +-- file .gitignore </br>

### Running the code:
1. Open the "src" folder.
2. Open the file named as "main.py" and run it. </br>
3. Next tun generate_images.py. This performs data augmentation. </br> 
4. Run "cnn_model.py" next. </br>
5. Now use the Intel model_optimizer and generate xml and bin files for the model. The generated xml and bin files should be in the "src" folder. The command line commands for the model optimizer are given further below. </br>
6. Finally <u> run "final.py" from the cmd window </u> for performing inference. </br>

### Output generated:
1. Creates a folder called "output". </br>
2. This folder contains the csv file generated (ACUTE_INFARCTS_Updated.csv and Inference_Data_GroundTruths.csv) and used by the code and also contains 2 other folders called "CLEANED_DATA" and "Infer_data". </br>
3. "CLEANED_DATA" contains folders folders named as the location of the brain infarcts and each of these folders contains the brain images of the person who has an infarcts at that particular location. </br>
4. "CLEANED_DATA" also contains the "test" and "train" folders which has data used by the CNN model. </br>
5. "Infer_data" folder contains the data to be used during inference. </br>
6. In the "src" folder, the model files which are generated are saved. </br>

### CMD Commands:
1. To generate an XML and bin file: </br>
&nbsp; &nbsp; a. Run the setupvars.bat file to initialize the OpenVino Environment. </br>
&nbsp; &nbsp; b. Go to the model optimizer folder in IntelSWTools and run: python mo_tf.py --input_model <input_model_destination>.pb -b 1 --output_dir <output_directory> --scale 255 --data_type FP32
2. To obtain an inference on the input image: </br>
&nbsp; &nbsp; a. python inference_test.py -m <model_destination>.xml -i <input_image>