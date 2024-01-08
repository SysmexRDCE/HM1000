#!/usr/bin/env python


#streamlit run ./app.py --server.maxUploadSize=5000
import base64
import imagej
from PIL import Image
import streamlit as st
import pickle
def pickle_all(key, value):
    pickle_out = open(key + ".pkl", "wb")
    pickle.dump(value, pickle_out)
    pickle_out.close()

st.title('N2V model app ')
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

selectbox=st.multiselect('Select tif file  from your directory',onlyfiles)

deletefile=selectbox
if st.button('Delete selected files '):
    for i in deletefile:
        os.system(f'rm -f ./input/{i}')
        st.write(f'{i} removed')

if (uploaded_file!=None) or (selectbox!=[]):
    import matplotlib.pyplot as plt
    import tifffile
    try:
        tiff_file = plt.imread(uploaded_file)


        tifffile.imsave(f'input/{filename}.tif', tiff_file)
        selectedtiff=[f'{filename}.tif']
    except:
        pass
    import warnings

    warnings.filterwarnings("ignore")

    if selectbox!=[]:
        selectedtiff=selectbox
    pickle_all('selectedtiff', selectedtiff)

    import base64

    img = Image.open(f'{pwd}/input/{selectedtiff[0]}')

    for i in range(1):
        try:
            img.seek(i)
            img.save('./output_jpeg/page1.tif')
            img00 = img.seek(i)

        except:
            pass

    subtract_range = st.slider("Select subtraction range", 1, 60, value=15)

    pickle_all('subtract_range', subtract_range)
    #os.system(f'python ./background_thresholding.py')
    st.write('original image')
    #st.image(f"{pwd}/output_jpeg/ORG.png")
    st.write('subtracted image')
    #st.image(f"{pwd}/output_jpeg/SUB.png")
    if st.button('Run'):
        step=1
        for i in [1,11,2,3,4,5,6,99]:
            os.system(f'python ./pyimagejapp{i}.py')
            if i==99:
                st.write('noiseless image')
                st.image(f'./output_jpeg/page7_0.png')
            st.write(f'{step} out of 10 steps completed ...')
            step=step+1
        st.write('To copy the N2V output, copy and paste the following command to the command line.')
        st.code("docker cp . .")
        st.write('Click the link below to download the Thunderstorm output')
        #os.system('python ./thunderstorm.py')
        import base64
        try:
            os.system('rm output.tar')
        except:
            pass
        os.system('tar -cf ./output.tar ./sri_files')
        with open("output.tar", "rb") as f:
            bytes = f.read()
            b64 = base64.b64encode(bytes).decode()
            href = f'<a href="data:file/tar;base64,{b64}">Download File</a> (right-click and save as output.tar)'
            st.markdown('Download')
            st.markdown(href, unsafe_allow_html=True)






