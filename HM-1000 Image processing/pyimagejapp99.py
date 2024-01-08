
from PIL import Image
import imagej
import os
import pickle
pwd = os.getcwd()
pickle_in = open(f'{pwd}/selectedtiff.pkl', 'rb')
selectedtiff = pickle.load(pickle_in)


mypath = pwd + '/input'
import imagej
from os import listdir
from os.path import isfile, join


onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

import tifftools

input1 = tifftools.read_tiff(f'{pwd}/output_step3/page_0.tif')

for i in range(1, 5000):
    input2 = tifftools.read_tiff(f'{pwd}/output_step3/page_{i}.tif')
    # Add input2 to input1
    input1['ifds'].extend(input2['ifds'])
os.system(f'rm -rf {pwd}/tiff_output/')
os.system(f'mkdir {pwd}/tiff_output/')
tifftools.write_tiff(input1, f'{pwd}/tiff_output/output_N2V.tif')





