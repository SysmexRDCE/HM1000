
from PIL import Image
import imagej
import os
import pickle
import pandas as pd
pwd = os.getcwd()
pickle_in = open(f'{pwd}/name_of_tiff_file.pkl', 'rb')
name_of_tiff_file = pickle.load(pickle_in)
pickle_in=open(f'{pwd}/subtrantion_range.pkl','rb')
sub_range=pickle.load(pickle_in)

mypath = pwd + '/input'
import imagej
from os import listdir
from os.path import isfile, join


onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
import os.path

import time

file_path= './output_jpeg/Results1.csv'

while not os.path.exists(file_path):
   time.sleep(1)
df1=pd.read_csv('./output_jpeg/Results1.csv')
sub1 = df1['Mean'][0]*sub_range
sub1000 = df1['Mean'][1]*sub_range
sub2000 = df1['Mean'][2]*sub_range
sub3000 = df1['Mean'][3]*sub_range
sub4000 = df1['Mean'][4]*sub_range
sub5000 = df1['Mean'][5]*sub_range


try:
    os.system('rm -f ./subtraction_macro.ijm')
except:
    pass

for sub,i in zip([sub1,sub1000,sub2000,sub3000,sub4000,sub5000],[1,1000,2000,3000,4000,5000]):
    macro1=f'''
run("Duplicate...", "duplicate range={i}-{i}");
run("3-3-2 RGB");    
run("Subtract Background...", "rolling=60");
saveAs("TIFF", "/Users/macbookpro/PycharmProjects/pyimagej/output_jpeg/image{i}.tif");
run("Subtract...", "value={sub}");
saveAs("PNG", "/Users/macbookpro/PycharmProjects/pyimagej/output_jpeg/image{i}.png");
close(); 
'''
    f = open('./subtraction_macro.ijm', 'a')
    f.write('\n' + macro1)
    f.close()