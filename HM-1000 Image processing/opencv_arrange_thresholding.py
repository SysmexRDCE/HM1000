
from PIL import Image
import imagej
import os
import pickle
pwd = os.getcwd()

mypath = pwd + '/input'
import imagej
from os import listdir
from os.path import isfile, join
pickle_in = open(f'{pwd}/onlyfiles1.pkl', 'rb')
selectedtiff = pickle.load(pickle_in)

IJ = imagej.init('/Applications/Fiji.app')
for img0 in [488,561]:
    for i in [0, 500, 1000, 2000, 3000, 4000, 4999]:
        macro0 = f'''open("/Users/macbookpro/PycharmProjects/pyimagej/output_step/thresh{img0}_{i}.png");
    run("3-3-2 RGB");
    open("/Users/macbookpro/PycharmProjects/pyimagej/output_step/{img0}merge{i}.tif");
    run("3-3-2 RGB");
    
    run("Images to Stack", "name=Stack title=[] use");
    run("Make Montage...", "columns=2 rows=1 scale=0.50");
    saveAs("PNG", "/Users/macbookpro/PycharmProjects/pyimagej/arange_img/Montage{img0}{i}.png");
    close();
    close();
    '''

        IJ.py.run_macro(macro0)














