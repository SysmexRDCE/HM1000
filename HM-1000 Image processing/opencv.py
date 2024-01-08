#!/usr/bin/env python

#streamlit run ./opencv.py --server.maxUploadSize=5000
import cv2
import pandas as pd
from PIL import Image
from PIL import Image
import base64
import os
import json
import pickle
import uuid
import re
import numpy as np
from os import listdir
from os.path import isfile, join
import streamlit as st
import pickle
import cv2
from cv2_rolling_ball import subtract_background_rolling_ball
pwd='.'
pickle_in = open(f'model_488.pkl', 'rb')
model_488 = pickle.load(pickle_in)
pickle_in = open(f'model_561.pkl', 'rb')
model_561 = pickle.load(pickle_in)
df_488=pd.read_csv('df_488.csv')
df_561=pd.read_csv('df_561.csv')
def pickle_all(key, value):
    pickle_out = open(key + ".pkl", "wb")
    pickle.dump(value, pickle_out)
    pickle_out.close()
df_488.drop(['Unnamed: 0'],axis=1,inplace=True)
df_561.drop(['Unnamed: 0'],axis=1,inplace=True)
df=pd.DataFrame()
for i in [1,300,500,1000,2000,3000,4000,4999]:
    df=pd.concat([df,df_561[df_561.index==i]],axis=0)
df1=pd.DataFrame()
for i in [1,300,500,1000,2000,3000,4000,4999]:
    df1=pd.concat([df1,df_488[df_488.index==i]],axis=0)
st.title('N2V and Thresholding model app ')
uploaded_file = st.file_uploader('FILE UPLOAD',accept_multiple_files=True)


import os

pwd = os.getcwd()

mypath = pwd + '/input'

from os import listdir
from os.path import isfile, join
mypath_cloud='/Users/macbookpro/Desktop/OneDrive/Images_2ndStudy_200122/1_Input'
onlyfiles_cloud = [f for f in listdir(mypath_cloud)]
select_folder_to_copy=st.selectbox('Select folder  from cloud directory',onlyfiles_cloud)
mypath_cloud_files=f'/Users/macbookpro/Desktop/OneDrive/Images_2ndStudy_200122/1_Input/{select_folder_to_copy}'
st.write(f'{select_folder_to_copy}')
onlyfiles_cloud_filess = [f for f in listdir(mypath_cloud_files) if isfile(join(mypath_cloud_files, f))]
st.write(f'{onlyfiles_cloud_filess}')
if st.button('Copy to local'):
    os.system(f'cp {mypath_cloud_files}/* ./input/' )
st.title('OR')
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

selectbox=st.multiselect('Select tif file  from your directory',onlyfiles)
if len(uploaded_file)==2 or (selectbox!=[]):
    import matplotlib.pyplot as plt
    import tifffile
    try:
        tiff_file1 = plt.imread(uploaded_file[0])
        tiff_file2 = plt.imread(uploaded_file[1])


        tifffile.imsave(f'input/488_image.tif', tiff_file1)
        tifffile.imsave(f'input/561_image.tif', tiff_file2)
        selectedtiff=[f'488_image.tif','561_image.tif']
    except:
        pass
    import warnings

    warnings.filterwarnings("ignore")

deletefile=selectbox
if st.button('Delete selected files '):
    for i in deletefile:
        os.system(f'rm -f ./input/{i}')
        st.write(f'{i} removed')

threshold_range_488 = st.sidebar.slider('threshold range 488', min_value=2.0, max_value=15.0, value=4.40)
threshold_range_561 = st.sidebar.slider('threshold range 561', min_value=2.0, max_value=15.0, value=3.50)
image1 = st.sidebar.number_input('image_488 1 subtraction threshold',value=df1['image_thresholding_value_488'][1])
image300 = st.sidebar.number_input('image_488 300 subtraction threshold',value=df1['image_thresholding_value_488'][300])
image1000 = st.sidebar.number_input('image_488 1000 subtraction threshold',value=df1['image_thresholding_value_488'][1000])
image2000 = st.sidebar.number_input('image_488 2000 subtraction threshold',value=df1['image_thresholding_value_488'][2000])
image3000 = st.sidebar.number_input('image_488 3000 subtraction threshold',value=df1['image_thresholding_value_488'][3000])
image4000 = st.sidebar.number_input('image_488 4000 subtraction threshold',value=df1['image_thresholding_value_488'][4000])
image5000 = st.sidebar.number_input('image_488 5000 subtraction threshold',value=df1['image_thresholding_value_488'][4999])
image1_561 = st.sidebar.number_input('image_561 1 subtraction threshold',value=df['image_thresholding_value_561'][1])
image300_561 = st.sidebar.number_input('image_561 300 subtraction threshold',value=df['image_thresholding_value_561'][300])
image1000_561 = st.sidebar.number_input('image_561 1000 subtraction threshold',value=df['image_thresholding_value_561'][1000])
image2000_561 = st.sidebar.number_input('image_561 2000 subtraction threshold',value=df['image_thresholding_value_561'][2000])
image3000_561 = st.sidebar.number_input('image_561 3000 subtraction threshold',value=df['image_thresholding_value_561'][3000])
image4000_561 = st.sidebar.number_input('image_561 4000 subtraction threshold',value=df['image_thresholding_value_561'][4000])
image5000_561 = st.sidebar.number_input('image_561 5000 subtraction threshold',value=df['image_thresholding_value_561'][4999])
mypath1 ='./input'
try:
    if len(selectbox)==2:
        onlyfiles1 = selectbox
    else:
        onlyfiles1 = selectedtiff
except:
    onlyfiles1 = selectbox

st.write(onlyfiles1)
pickle_all('onlyfiles1',onlyfiles1)
pickle_in = open(f'{pwd}/onlyfiles1.pkl', 'rb')
selectedtiff = pickle.load(pickle_in)
if st.button('Background Subtraction'):
    st.write('Background subtraction may take several minutes')
    os.system('python ./background_thresholding.py')
    st.write('Background subtraction done !!')
if True:
    if st.button('Divide'):



        img = Image.open(f'input/{onlyfiles1[0]}')
        img1=Image.open(f'input/{onlyfiles1[1]}')
        for i in range(5000):
                    try:
                        img.seek(i)
                        img.save(f'./output_step/488merge{i}.tif')
                        img1.seek(i)
                        img1.save(f'./output_step/561merge{i}.tif')
                        print(f'slice {i}')
                        if i in [1000,2000,3000,4000,4999]:
                            st.write(f'slice {i} done')
                    except EOFError:
                         break
    if st.button('Arange Thresholding'):
        os.system('rm -f ./arange_img/*')
        for i in [0,500,1000,2000,3000,4000,4999]:

            img_path_488 = f'./output_step/488merge{i}.tif'
            img_path_561 = f'./output_step/561merge{i}.tif'
            img = cv2.imread(img_path_488,cv2.IMREAD_ANYDEPTH)


            img1 = cv2.imread(img_path_561,cv2.IMREAD_ANYDEPTH)
            #img, background = subtract_background_rolling_ball(img, 10, light_background=True,
                                                               #use_paraboloid=False, do_presmooth=True)
            #img1, background = subtract_background_rolling_ball(img1, 50, light_background=False,
             #                                                   use_paraboloid=False, do_presmooth=False)
            image1 = img.mean() + threshold_range_488 * img.std()
            image1_561 = img1.mean() + threshold_range_561 * img1.std()

            ret, thresh488 = cv2.threshold(img, image1, 255, cv2.THRESH_TOZERO)
            ret, thresh561 = cv2.threshold(img1, image1_561, 255, cv2.THRESH_TOZERO)
            ret, thresh561_ = cv2.threshold(img1, image1_561, 255, cv2.THRESH_TOZERO_INV)
            thresh488 = thresh488 + thresh561_
            ret, thresh488 = cv2.threshold(img, image1, 255, cv2.THRESH_TOZERO)

            cv2.imwrite(f'./output_step/thresh488_{i}.png', thresh488)
            cv2.imwrite(f'./output_step/thresh561_{i}.png', thresh561)
        st.write('Starting Imagej')
        os.system('python opencv_arrange_thresholding.py')
        for png in [488, 561]:
            for i in [0, 500, 1000, 2000, 3000, 4000, 4999]:
                st.caption(f'{png} {i+1} image')
                st.image(f'./arange_img/Montage{png}{i}.png',width=900)
        #os.system(f'rm -f ./output_step/Montage{png}{i}.png')


    if st.button('Auto Thresholding'):
        ##################

        ################
        df_488=pd.DataFrame()
        image_num_488=[]
        image_mean_488=[]
        image_std_488=[]
        image_thresholding_value_488=[]
        image_max_488=[]
        image_min_488=[]
        df_561 = pd.DataFrame()
        image_num_561 = []
        image_mean_561 = []
        image_std_561 = []
        image_thresholding_value_561 = []
        image_max_561 = []
        image_min_561 = []
        if True:
            for i in range(5000):
                img_path_561 = f'./output_step/561merge{i}.tif'
                img_path_488 = f'./output_step/488merge{i}.tif'
                img = cv2.imread(img_path_488,cv2.IMREAD_ANYDEPTH)


                img1 = cv2.imread(img_path_561,cv2.IMREAD_ANYDEPTH)

                #img, background = subtract_background_rolling_ball(img, 10, light_background=True,
                                                                  # use_paraboloid=False, do_presmooth=True)
               # img1, background = subtract_background_rolling_ball(img1, 50, light_background=False,
                #                                                   use_paraboloid=False, do_presmooth=False)
                df_488_stream=pd.DataFrame()
                df_488_stream['image_num_488'] = [i]
                df_488_stream['image_mean_488']=[np.mean(img)]

                df_488_stream['image_std_488']=[np.std(img)]
                df_488_stream['image_max_488']=[np.max(img)]
                df_488_stream['image_min_488']=[np.min(img)]
                y_pred_488=model_488.predict(df_488_stream[['image_mean_488','image_std_488']])
                df_488_stream['y_pred_488']=y_pred_488

                df_561_stream = pd.DataFrame()
                df_561_stream['image_num_561'] = [i]
                df_561_stream['image_mean_561'] = [np.mean(img1)]

                df_561_stream['image_std_561'] = [np.std(img1)]
                df_561_stream['image_max_561'] = [np.max(img1)]
                df_561_stream['image_min_561'] = [np.min(img1)]
                y_pred_561 = model_561.predict(df_561_stream[['image_mean_561','image_std_561']])
                df_561_stream['y_pred_561']=y_pred_561
                print(f'thresholding {i}')

                if i in [1,500,1000,2000,3000,4000,4999]:

                    st.table(df_488_stream)
                    st.table(df_561_stream)




                image1 = y_pred_488[0]
                image1_561 = y_pred_561[0]
                image1 = img.mean() + threshold_range_488 * img.std()
                image1_561 = img1.mean() + threshold_range_561 * img1.std()
                image_mean_488.append(np.mean(img))
                image_num_488.append(img)
                image_std_488.append(np.std(img))
                image_thresholding_value_488.append(image1)
                image_max_488.append(np.max(img))
                image_min_488.append(np.min(img))

                image_mean_561.append(np.mean(img1))
                image_num_561.append(img1)
                image_std_561.append(np.std(img1))
                image_thresholding_value_561.append(image1_561)
                image_max_561.append(np.max(img1))
                image_min_561.append(np.min(img1))
                ret, thresh488 = cv2.threshold(img, image1, 255, cv2.THRESH_TOZERO)
                ret, thresh561 = cv2.threshold(img1, image1_561, 255, cv2.THRESH_TOZERO)
                ret, thresh561_ = cv2.threshold(img1, image1_561, 255, cv2.THRESH_TOZERO_INV)
                thresh488 = thresh488 + thresh561_
                ret, thresh488 = cv2.threshold(img, image1, 255, cv2.THRESH_TOZERO)
                cv2.imwrite(f'./output_step/thresh488_{i}.tif', thresh488)
                cv2.imwrite(f'./output_step/thresh561_{i}.tif', thresh561)



            df_488['image_mean_488']=image_mean_488
            df_488['image_num_488']=image_num_488
            df_488['image_std_488']=image_std_488
            df_488['image_max_488']=image_max_488
            df_488['image_min_488']=image_min_488
            df_488['image_thresholding_value_488']=image_thresholding_value_488

            df_561['image_mean_561'] = image_mean_561
            df_561['image_num_561'] = image_num_561
            df_561['image_std_561'] = image_std_561
            df_561['image_max_561'] = image_max_561
            df_561['image_min_561'] = image_min_561
            df_561['image_thresholding_value_561'] = image_thresholding_value_561



    if st.button('manuel Thresholding'):
        df_488 = pd.DataFrame()
        image_num_488 = []
        image_mean_488 = []
        image_std_488 = []
        image_thresholding_value_488 = []
        image_max_488 = []
        image_min_488 = []
        df_561 = pd.DataFrame()
        image_num_561 = []
        image_mean_561 = []
        image_std_561 = []
        image_thresholding_value_561 = []
        image_max_561 = []
        image_min_561 = []



        if True:
            minus1 = (image1-image300)/300
            minus300 = (image300 - image1000)/700
            minus1000 = (image1000-image2000)/1000
            minus2000 = (image2000-image3000)/1000
            minus3000 = (image3000-image4000)/1000
            minus4000 = (image4000-image5000)/1000
            minus1_561 = (image1_561-image300_561)/300
            minus300_561 = (image300_561 - image1000_561) / 700
            minus1000_561 = (image1000_561-image2000_561)/1000
            minus2000_561 = (image2000_561-image3000_561)/1000
            minus3000_561 = (image3000_561-image4000_561)/1000
            minus4000_561 = (image4000_561-image5000_561)/1000
            for i in range(5000):
                img_path_561=f'./output_step/561merge{i}.tif'
                img_path_488=f'./output_step/488merge{i}.tif'
                img = cv2.imread(img_path_488)

                img1 = cv2.imread(img_path_561)
                image_mean_488.append(np.mean(img))
                image_num_488.append(i)
                image_std_488.append(np.std(img))

                image_max_488.append(np.max(img))
                image_min_488.append(np.min(img))

                image_mean_561.append(np.mean(img1))
                image_num_561.append(i)
                image_std_561.append(np.std(img1))

                image_max_561.append(np.max(img1))
                image_min_561.append(np.min(img1))

                if i in [1,1000, 2000, 3000, 4000, 4999]:
                    st.write(f'threshold {i} done')
                    st.write(f'mean of 488 {np.mean(img)}')
                    st.write(f'mean of 561 {np.mean(img1)}')
                if i < 300:
                    image1 = image1 - minus1
                    image1_561 = image1_561 - minus1_561
                    image_thresholding_value_488.append(image1)
                    image_thresholding_value_561.append(image1_561)
                    ret, thresh488 = cv2.threshold(img, image1, 255, cv2.THRESH_TOZERO)
                    ret, thresh561 = cv2.threshold(img1, image1_561, 255, cv2.THRESH_TOZERO)
                    ret, thresh561_ = cv2.threshold(img1, image1_561, 255, cv2.THRESH_TOZERO_INV)
                    thresh488 = thresh488 + thresh561_
                    ret, thresh488 = cv2.threshold(img, image1, 255, cv2.THRESH_TOZERO)
                    cv2.imwrite(f'./output_step/thresh488_{i}.tif', cv2.cvtColor(thresh488, 6))
                    cv2.imwrite(f'./output_step/thresh561_{i}.tif', cv2.cvtColor(thresh561, 6))
                elif i < 1000:
                    image1 = image1 - minus300
                    image1_561=image1_561-minus300_561
                    image_thresholding_value_488.append(image1)
                    image_thresholding_value_561.append(image1_561)
                    ret, thresh488 = cv2.threshold(img, image1, 255, cv2.THRESH_TOZERO)
                    ret, thresh561 = cv2.threshold(img1, image1_561, 255, cv2.THRESH_TOZERO)
                    ret, thresh561_ = cv2.threshold(img1, image1_561, 255, cv2.THRESH_TOZERO_INV)
                    thresh488 = thresh488 + thresh561_
                    ret, thresh488 = cv2.threshold(img, image1, 255, cv2.THRESH_TOZERO)
                    cv2.imwrite(f'./output_step/thresh488_{i}.tif', cv2.cvtColor(thresh488, 6))
                    cv2.imwrite(f'./output_step/thresh561_{i}.tif', cv2.cvtColor(thresh561, 6))

                elif i < 2000 and i > 999:
                    image1000 = image1000 - minus1000
                    image1000_561 = image1000_561 - minus1000_561
                    image_thresholding_value_488.append(image1000)
                    image_thresholding_value_561.append(image1000_561)
                    ret, thresh488 = cv2.threshold(img, image1000, 255, cv2.THRESH_TOZERO)
                    ret, thresh561 = cv2.threshold(img1, image1000_561, 255, cv2.THRESH_TOZERO)
                    ret, thresh561_ = cv2.threshold(img1, image1000_561, 255, cv2.THRESH_TOZERO_INV)
                    thresh488 = thresh488 + thresh561_
                    ret, thresh488 = cv2.threshold(img, image1000, 255, cv2.THRESH_TOZERO)
                    cv2.imwrite(f'./output_step/thresh488_{i}.tif', cv2.cvtColor(thresh488, 6))
                    cv2.imwrite(f'./output_step/thresh561_{i}.tif', cv2.cvtColor(thresh561, 6))
                elif i < 3000 and i > 1999:
                    image2000 = image2000 - minus2000
                    image2000_561 = image2000_561 - minus2000_561
                    image_thresholding_value_488.append(image2000)
                    image_thresholding_value_561.append(image2000_561)
                    ret, thresh488 = cv2.threshold(img, image2000, 255, cv2.THRESH_TOZERO)
                    ret, thresh561 = cv2.threshold(img1, image2000_561, 255, cv2.THRESH_TOZERO)
                    ret, thresh561_ = cv2.threshold(img1, image2000_561, 255, cv2.THRESH_TOZERO_INV)
                    thresh488 = thresh488 + thresh561_
                    ret, thresh488 = cv2.threshold(img, image2000, 255, cv2.THRESH_TOZERO)
                    cv2.imwrite(f'./output_step/thresh488_{i}.tif', cv2.cvtColor(thresh488, 6))
                    cv2.imwrite(f'./output_step/thresh561_{i}.tif', cv2.cvtColor(thresh561, 6))
                elif i < 4000 and i > 2999:
                    image3000 = image3000 - minus3000
                    image3000_561 = image3000_561 - minus3000_561
                    image_thresholding_value_488.append(image3000)
                    image_thresholding_value_561.append(image3000_561)
                    ret, thresh488 = cv2.threshold(img, image3000, 255, cv2.THRESH_TOZERO)
                    ret, thresh561 = cv2.threshold(img1, image3000_561, 255, cv2.THRESH_TOZERO)
                    ret, thresh561_ = cv2.threshold(img1, image3000_561, 255, cv2.THRESH_TOZERO_INV)
                    thresh488 = thresh488 + thresh561_
                    ret, thresh488 = cv2.threshold(img, image3000, 255, cv2.THRESH_TOZERO)
                    cv2.imwrite(f'./output_step/thresh488_{i}.tif', cv2.cvtColor(thresh488, 6))
                    cv2.imwrite(f'./output_step/thresh561_{i}.tif', cv2.cvtColor(thresh561, 6))
                elif i < 5001 and i > 3999:
                    image4000 = image4000 - minus4000

                    image4000_561 = image4000_561 - minus4000_561
                    image_thresholding_value_488.append(image4000)
                    image_thresholding_value_561.append(image4000_561)
                    ret, thresh488 = cv2.threshold(img, image4000, 255, cv2.THRESH_TOZERO)
                    ret, thresh561 = cv2.threshold(img1, image4000_561, 255, cv2.THRESH_TOZERO)
                    ret, thresh561_ = cv2.threshold(img1, image4000_561, 255, cv2.THRESH_TOZERO_INV)
                    thresh488 = thresh488 + thresh561_
                    ret, thresh488 = cv2.threshold(img, image4000, 255, cv2.THRESH_TOZERO)
                    cv2.imwrite(f'./output_step/thresh488_{i}.tif', cv2.cvtColor(thresh488, 6))
                    cv2.imwrite(f'./output_step/thresh561_{i}.tif', cv2.cvtColor(thresh561, 6))
            df_488['image_mean_488'] = image_mean_488
            df_488['image_num_488'] = image_num_488
            df_488['image_std_488'] = image_std_488
            df_488['image_max_488'] = image_max_488
            df_488['image_min_488'] = image_min_488
            df_488['image_thresholding_value_488'] = image_thresholding_value_488

            df_561['image_mean_561'] = image_mean_561
            df_561['image_num_561'] = image_num_561
            df_561['image_std_561'] = image_std_561
            df_561['image_max_561'] = image_max_561
            df_561['image_min_561'] = image_min_561
            df_561['image_thresholding_value_561'] = image_thresholding_value_561
            df_488.to_csv('df_488.csv')
            df_561.to_csv('df_561.csv')
            print(f'threshold {i}')
    if st.button('Merge'):
            import tifftools

            input488_1 = tifftools.read_tiff(f'{pwd}/output_step/thresh488_0.tif')
            input561_1 = tifftools.read_tiff(f'{pwd}/output_step/thresh561_0.tif')
            for i in range(1, 5000):
                input488_2 = tifftools.read_tiff(f'{pwd}/output_step/thresh488_{i}.tif')
                input561_2 = tifftools.read_tiff(f'{pwd}/output_step/thresh561_{i}.tif')
                # Add input2 to input1
                input488_1['ifds'].extend(input488_2['ifds'])
                input561_1['ifds'].extend(input561_2['ifds'])
                print(f' added {i}')
                if i in [1000, 2000, 3000, 4000, 4999]:
                    st.write(f'merge {i} done')
            try:
                os.system('rm -fr ./tiff_output/')
                os.system('mkdir ./tiff_output/')
            except:
                pass
            tifftools.write_tiff(input488_1, f'{pwd}/tiff_output/488_opencv_sub.tif')
            tifftools.write_tiff(input561_1, f'{pwd}/tiff_output/561_opencv_sub.tif')
    if st.button('create thunderstorm image'):
        os.system('python thunderstorm00.py')
    if st.button('upload cloud'):
        try:
            os.system(f'rm -rf  /Users/macbookpro/Desktop/OneDrive/Images_2ndStudy_200122/3_Results/{select_folder_to_copy}')
            st.write(f'{select_folder_to_copy} folder removed')
        except:
            st.write(f'{mypath_cloud_files} No path')

        os.system(f'mkdir /Users/macbookpro/Desktop/OneDrive/Images_2ndStudy_200122/3_Results/{select_folder_to_copy}')
        st.write(f'{select_folder_to_copy} folder created')
        ## clean_tiff
        try:


            file_path_cloud=f'/Users/macbookpro/Desktop/OneDrive/Images_2ndStudy_200122/3_Results/{select_folder_to_copy}'
            os.system(f'cp {pwd}/tiff_output/488_opencv_sub.tif {file_path_cloud}/output_{selectbox[0]}')
            os.system(f'cp {pwd}/tiff_output/561_opencv_sub.tif {file_path_cloud}/output_{selectbox[1]}')
            st.write(f'{selectbox} copied to the cloud')
        except:
            st.write('file did not copied')
        try:
            ## sri files
            os.system(f'cp /Users/macbookpro/PycharmProjects/pyimagej/sri_files/488_Normalized_Gaussian.tif {file_path_cloud}/Normalized_Gaussian_{selectbox[0]}')
            os.system(f'cp /Users/macbookpro/PycharmProjects/pyimagej/sri_files/561_Normalized_Gaussian.tif {file_path_cloud}/Normalized_Gaussian_{selectbox[1]}')
            st.write(f'Normalized_Gaussian copied to the cloud')
        except:
            st.write(f'Normalized_Gaussian did not copied to the cloud')
        try:
            ##csv files
            os.system(f'cp /Users/macbookpro/PycharmProjects/pyimagej/csv_files/488_ThunderSTORM_results.csv {file_path_cloud}/488_ThunderSTORM_results.csv')
            os.system(f'cp /Users/macbookpro/PycharmProjects/pyimagej/csv_files/561_ThunderSTORM_results.csv {file_path_cloud}/561_ThunderSTORM_results.csv')
            st.write(f'csv files copied to the cloud')

            df_csv_488=pd.read_csv('df_488.csv')
            df_csv_561 = pd.read_csv('df_561.csv')
            df_488=pd.concat(df_csv_488,df_488,axis=0)
            df_488.reset_index(drop=True,inplace=True)
            df_561 = pd.concat(df_csv_561, df_561, axis=0)
            df_561.reset_index(drop=True, inplace=True)
            df_488.to_csv('df_488.csv')
            df_561.to_csv('df_561.csv')
        except:
            st.write(f'csv files did not copied to the cloud')
    if st.button('Train Model'):
        os.system(f'ipython linear_regression.ipynb')
            # st.write('Done')
    # the window showing output images
    # with the corresponding thresholding
    # techniques applied to the input images








