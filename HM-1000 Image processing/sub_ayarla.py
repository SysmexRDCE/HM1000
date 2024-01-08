import os
import streamlit as st
try:
    os.system('rm ./sub_ayarla.ijm')
    os.system('touch ./sub_ayarla.ijm')
except:
    pass
name_of_tiff_file= '488_HER2 protocolo dilucion 1-2 2min'
macro = f'''

    open("/Users/macbookpro/PycharmProjects/pyimagej/input/{name_of_tiff_file}.tif");
     '''
f = open('sub_ayarla.ijm', 'a')
f.write('\n' + macro)
f.close()
for i in [1,100,500,1000,2000,3000,4000,5000]:
    macro=f'''
    selectWindow("{name_of_tiff_file}.tif");
    run("Duplicate...", "duplicate range={i}-{i}");
    run("Subtract Background...", "rolling=5");
    run("3-3-2 RGB");
    saveAs("Tiff", "/Users/macbookpro/PycharmProjects/pyimagej/sub_ayarlama/sub_ayarla{i}.tif");
    
    '''
    f = open('sub_ayarla.ijm', 'a')
    f.write('\n' + macro)
    f.close()

