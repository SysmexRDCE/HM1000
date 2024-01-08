
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

macro0 = f'''open("/Users/macbookpro/PycharmProjects/pyimagej/input/{selectedtiff[0]}");
run("Subtract Background...", "rolling=10 stack");
run("Save");
close();
open("/Users/macbookpro/PycharmProjects/pyimagej/input/{selectedtiff[1]}");
run("Subtract Background...", "rolling=10 stack");
run("Save");
close();
'''

IJ.py.run_macro(macro0)















