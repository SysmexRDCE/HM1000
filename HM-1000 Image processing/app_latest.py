import os

import cv2
import streamlit as st
#!/usr/bin/env python

#streamlit run ./app_latest.py --server.maxUploadSize=5000
import base64
import imagej
from PIL import Image
import base64
import os
import json
import pickle
import uuid
import re

import streamlit as st
import pandas as pd
import streamlit as st
import pickle
def download_button(object_to_download, download_filename, button_text, pickle_it=False):
    """
    Generates a link to download the given object_to_download.
    Params:
    ------
    object_to_download:  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv,
    some_txt_output.txt download_link_text (str): Text to display for download
    link.
    button_text (str): Text to display on download button (e.g. 'click here to download file')
    pickle_it (bool): If True, pickle file.
    Returns:
    -------
    (str): the anchor tag to download object_to_download
    Examples:
    --------
    download_link(your_df, 'YOUR_DF.csv', 'Click to download data!')
    download_link(your_str, 'YOUR_STRING.txt', 'Click to download text!')
    """
    if pickle_it:
        try:
            object_to_download = pickle.dumps(object_to_download)
        except pickle.PicklingError as e:
            st.write(e)
            return None

    else:
        if isinstance(object_to_download, bytes):
            pass

        elif isinstance(object_to_download, pd.DataFrame):
            object_to_download = object_to_download.to_csv(index=False)

        # Try JSON encode for everything else
        else:
            object_to_download = json.dumps(object_to_download)

    try:
        # some strings <-> bytes conversions necessary here
        b64 = base64.b64encode(object_to_download.encode()).decode()

    except AttributeError as e:
        b64 = base64.b64encode(object_to_download).decode()

    button_uuid = str(uuid.uuid4()).replace('-', '')
    button_id = re.sub('\d+', '', button_uuid)

    custom_css = f""" 
        <style>
            #{button_id} {{
                background-color: rgb(255, 255, 255);
                color: rgb(38, 39, 48);
                padding: 0.25em 0.38em;
                position: relative;
                text-decoration: none;
                border-radius: 4px;
                border-width: 1px;
                border-style: solid;
                border-color: rgb(230, 234, 241);
                border-image: initial;
            }} 
            #{button_id}:hover {{
                border-color: rgb(246, 51, 102);
                color: rgb(246, 51, 102);
            }}
            #{button_id}:active {{
                box-shadow: none;
                background-color: rgb(246, 51, 102);
                color: white;
                }}
        </style> """

    dl_link = custom_css + f'<a download="{download_filename}" id="{button_id}" href="data:file/txt;base64,{b64}">{button_text}</a><br></br>'

    return dl_link
def pickle_all(key, value):
    pickle_out = open(key + ".pkl", "wb")
    pickle.dump(value, pickle_out)
    pickle_out.close()

st.title('Macro Create app ')
uploaded_file = st.file_uploader('FILE UPLOAD')
if uploaded_file!=None:
    filename=st.text_input('write your file name ')
import os

pwd = os.getcwd()

mypath = pwd + '/input'

from os import listdir
from os.path import isfile, join

st.title('OR')
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

selectbox=st.selectbox('Select tif file  from your directory',onlyfiles)

deletefile=selectbox
if st.button('Delete selected files '):
    for i in deletefile:
        os.system(f'rm -f ./input/{i}')
        st.write(f'{i} removed')
os.system('rm ./macro_all_latest.ijm')
os.system('touch ./macro_all_latest.ijm')
try:
    os.system('rm ./sub_ayarla.ijm')
    os.system('touch ./sub_ayarla.ijm')
except:
    pass

name_of_tiff_file=selectbox
number_of_tiff = st.number_input('Tiff Size',value=5000)
macro = f'''

    open("{pwd}/input/{name_of_tiff_file}");
     '''
f = open('sub_ayarla.ijm', 'a')
f.write('\n' + macro)
f.close()
rolling=st.number_input('Background Subtraction rolling ',value=5)
if number_of_tiff==5000:
    for i in [5000,4000,3000,2000,1000,1]:
        macro1 = f'''
        selectWindow("{name_of_tiff_file}");
        run("Duplicate...", "duplicate range={i}-{i}");
        run("Subtract Background...", "rolling={rolling}");
        run("3-3-2 RGB");
        saveAs("Tiff", "{pwd}/sub_ayarlama/sub_ayarla{i}.tif");
        run("Measure");
    
        '''
        f = open('sub_ayarla.ijm', 'a')
        f.write('\n' + macro1)
        f.close()
    filename="sub_ayarla.ijm"
    with open(filename, "rb") as f:
        s = f.read()

    download_button_str = download_button(s, f'{filename}', f'Click here to download {filename}')
    st.markdown(download_button_str, unsafe_allow_html=True)
if number_of_tiff == 1000:
    for i in [1, 100, 500,1000]:
        macro1 = f'''
        selectWindow("{name_of_tiff_file}");
        run("Duplicate...", "duplicate range={i}-{i}");
        run("Subtract Background...", "rolling={rolling}");
        run("3-3-2 RGB");
        saveAs("Tiff", "{pwd}/sub_ayarlama/sub_ayarla{i}.tif");

        '''
        f = open('sub_ayarla.ijm', 'a')
        f.write('\n' + macro1)
        f.close()
    filename = "sub_ayarla.ijm"
    with open(filename, "rb") as f:
        s = f.read()

    download_button_str = download_button(s, f'{filename}', f'Click here to download {filename}')
    st.markdown(download_button_str, unsafe_allow_html=True)
macro=f'open("{pwd}/input/{name_of_tiff_file}"); '
only_name_of_file=name_of_tiff_file.split('.')[0]
f = open('macro_all.ijm', 'a')
f.write('\n' + macro)
f.close()
############################# all in one macro ###############
image1=st.number_input('image 1 subtraction threshold')
image1000=st.number_input('image 1000 subtraction threshold')
image2000=st.number_input('image 2000 subtraction threshold')
image3000=st.number_input('image 3000 subtraction threshold')
image4000=st.number_input('image 4000 subtraction threshold')
image5000=st.number_input('image 5000 subtraction threshold')

minus1 = (image1-image1000)/1000
minus1000 = (image1000-image2000)/1000
minus2000 = (image2000-image3000)/1000
minus3000 = (image3000-image4000)/1000
minus4000 = (image4000-image5000)/1000

macro=f'''open("/Users/macbookpro/PycharmProjects/pyimagej/input/{name_of_tiff_file}");

run("Duplicate...", "duplicate range=1-1");
run("Subtract Background...", "rolling={rolling}");
run("Subtract...", "value={image1}");
selectWindow("{name_of_tiff_file}");
run("Duplicate...", "duplicate range=2-2");
run("Subtract Background...", "rolling={rolling}");
run("Subtract...", "value={image1}");
run("Images to Stack", "name=Stack title=[] use");
selectWindow("{name_of_tiff_file}");
run("Duplicate...", "duplicate range=3-3");
run("Subtract Background...", "rolling={rolling}");
run("Subtract...", "value={image1}");
run("Concatenate...", "open image1=Stack image2=[{only_name_of_file}-1.tif] image3=[-- None --]");
selectWindow("{name_of_tiff_file}");
run("Duplicate...", "duplicate range=4-4");
run("Subtract Background...", "rolling={rolling}");
run("Subtract...", "value={image1}");
run("Concatenate...", "open image1=Untitled image2=[{only_name_of_file}-1.tif] image3=[-- None --]");
 '''
f = open('macro_all_latest.ijm', 'a')
f.write('\n' + macro)
f.close()
for i in range(5,number_of_tiff+1):

    if i<1000:
        image1=image1-minus1
        macro=f'''
selectWindow("{name_of_tiff_file}");
run("Duplicate...", "duplicate range={i}-{i}");
run("Subtract Background...", "rolling={rolling}");
run("Subtract...", "value={image1}");
run("Concatenate...", "open image1=Untitled image2=[{only_name_of_file}-1.tif] image3=[-- None --]");
'''
        f = open('macro_all_latest.ijm', 'a')

        f.write('\n' + macro)
        f.close()
    elif i<2000 and i>999:
        image1000=image1000-minus1000
        macro = f'''
        selectWindow("{name_of_tiff_file}");
        run("Duplicate...", "duplicate range={i}-{i}");
        run("Subtract Background...", "rolling={rolling}");
        run("Subtract...", "value={image1000}");
        run("Concatenate...", "open image1=Untitled image2=[{only_name_of_file}-1.tif] image3=[-- None --]");
        '''
        f = open('macro_all_latest.ijm', 'a')

        f.write('\n' + macro)
        f.close()
    elif i<3000 and i>1999:
        image2000=image2000-minus2000
        macro = f'''
        selectWindow("{name_of_tiff_file}");
        run("Duplicate...", "duplicate range={i}-{i}");
        run("Subtract Background...", "rolling={rolling}");
        run("Subtract...", "value={image2000}");
        run("Concatenate...", "open image1=Untitled image2=[{only_name_of_file}-1.tif] image3=[-- None --]");
        '''
        f = open('macro_all_latest.ijm', 'a')

        f.write('\n' + macro)
        f.close()
    elif i<4000 and i>2999:
        image3000=image3000-minus3000
        macro = f'''
        selectWindow("{name_of_tiff_file}");
        run("Duplicate...", "duplicate range={i}-{i}");
        run("Subtract Background...", "rolling={rolling}");
        run("Subtract...", "value={image3000}");
        run("Concatenate...", "open image1=Untitled image2=[{only_name_of_file}-1.tif] image3=[-- None --]");
        '''
        f = open('macro_all_latest.ijm', 'a')

        f.write('\n' + macro)
        f.close()
    elif i<5001 and i>3999:
        image4000=image4000-minus4000
        macro = f'''
        selectWindow("{name_of_tiff_file}");
        run("Duplicate...", "duplicate range={i}-{i}");
        run("Subtract Background...", "rolling={rolling}");
        run("Subtract...", "value={image4000}");
        run("Concatenate...", "open image1=Untitled image2=[{only_name_of_file}-1.tif] image3=[-- None --]");
        '''
        f = open('macro_all_latest.ijm', 'a')

        f.write('\n' + macro)
        f.close()
macro=f'saveAs("Tiff", "/Users/macbookpro/PycharmProjects/pyimagej/tiff_output/output_sub.tif");selectWindow("{name_of_tiff_file}");close();'
f = open('macro_all_latest.ijm', 'a')
f.write('\n' + macro)
f.close()

macro=f'''
run("Camera setup", "offset=100.0 isemgain=false photons2adu=0.46 pixelsize=130.0");
run("Run analysis", "filter=[Wavelet filter (B-Spline)] scale=2.0 order=3 detector=[Local maximum] connectivity=8-neighbourhood threshold=std(Wave.F1) estimator=[PSF: Integrated Gaussian] sigma=1.6 fitradius=3 method=[Weighted Least squares] full_image_fitting=false mfaenabled=false renderer=[Normalized Gaussian] dxforce=false magnification=5.0 dx=20.0 colorizez=false threed=false dzforce=false repaint=50");
run("Export results", "filepath={pwd}/csv_files/{only_name_of_file}_ThunderSTORM_results.csv fileformat=[CSV (comma separated)] sigma=true intensity=true chi2=true offset=true saveprotocol=true x=true y=true bkgstd=true id=true uncertainty=true frame=true");
selectWindow("Normalized Gaussian");
saveAs("Tiff", "{pwd}/sri_files/Normalized_Gaussian_of_{name_of_tiff_file}");
'''
f = open('macro_all_latest.ijm', 'a')
f.write('\n' + macro)
f.close()
filename="macro_all_latest.ijm"
with open(filename, "rb") as f:
    s = f.read()

download_button_str = download_button(s, f'{filename}', f'Click here to download {filename}')
st.markdown(download_button_str, unsafe_allow_html=True)
if st.button('Send files to Cloud'):
    try:
        os.system(f"mkdir /Users/macbookpro/Desktop/OneDrive/imagejresults/Output/{only_name_of_file.split('_')[0]}_6NEG_SR")
    except:
        pass
    try:

        os.system(f"mkdir /Users/macbookpro/Desktop/OneDrive/imagejresults/Output/{only_name_of_file.split('_')[0]}_6NEG_SR/{only_name_of_file.split('_')[3]}_6NEG")
    except:
        pass
    os.system(f"cp /Users/macbookpro/PycharmProjects/pyimagej/tiff_output/output_sub.tif  /Users/macbookpro/Desktop/OneDrive/imagejresults/Output/{only_name_of_file.split('_')[0]}_6NEG_SR/{only_name_of_file.split('_')[3]}_6NEG/{name_of_tiff_file}")
    os.system(f"cp /Users/macbookpro/PycharmProjects/pyimagej/sri_files/Normalized_Gaussian_of_{name_of_tiff_file}  /Users/macbookpro/Desktop/OneDrive/imagejresults/Output/{only_name_of_file.split('_')[0]}_6NEG_SR/{only_name_of_file.split('_')[3]}_6NEG/{only_name_of_file.split('_')[0]}_6NEG_SR_Normalized_Gaussian_of_{only_name_of_file.split('_')[3]}.tif")
    os.system(f"cp /Users/macbookpro/PycharmProjects/pyimagej/csv_files/*  /Users/macbookpro/Desktop/OneDrive/imagejresults/Output/{only_name_of_file.split('_')[0]}_6NEG_SR/{only_name_of_file.split('_')[3]}_6NEG/")
    try:
        os.system('rm -f ./csv_files/*')

    except:
        pass
if st.button('delete input files'):
    try:
        os.system(f"rm -f ./input/*")
    except:
        pass
import cv2
mypath1 = pwd + '/tiff_output'
onlyfiles1 = [f for f in listdir(mypath1) if isfile(join(mypath, f))]
merge_images = st.multiselect('Select for merge images_488_561 ', onlyfiles1)
if len(merge_images) == 2:

    img = Image.open(f'tiff_output/{merge_images[0]}')
    img1 = Image.open(f'tiff_output/{merge_images[1]}')
    st.write(f'tiff_output/{merge_images[1]}')
    for i in range(5000):
            try:
                img.seek(i)
                img1.seek(i)

                img.save(f'./output_step/488merge{i}.tif')
                img1.save(f'./output_step/561merge{i}.tif')
                img488 =cv2.imread(f'./output_step/488merge{i}.tif')
                img561=cv2.imread(f'./output_step/561merge{i}.tif')
                imgmerge=img488-img561
                cv2.imwrite(f'./output_step/merge{i}.tif',cv2.cvtColor(imgmerge, 6))
                print(f'image merge create {i}')
                if i in [500,1000,2000,3000,4000,5000]:
                    st.write(f'{i} merge finished')

            except EOFError:
                 break
    if True:
        import tifftools

        input1 = tifftools.read_tiff(f'{pwd}/output_step/merge0.tif')

        for i in range(1, 5000):
            input2 = tifftools.read_tiff(f'{pwd}/output_step/merge{i}.tif')
            # Add input2 to input1
            input1['ifds'].extend(input2['ifds'])
            print(f' added {i}')
        tifftools.write_tiff(input1, f'{pwd}/tiff_output/488_sub.tif')
        st.write('Done')