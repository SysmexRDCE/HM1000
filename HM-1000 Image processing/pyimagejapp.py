
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
IJ = imagej.init('/Applications/Fiji.app')
for tiff in selectedtiff:
            img = Image.open(f'input/{tiff}')

            for i in range(5000):
                try:
                    img.seek(i)
                    img.save('./output_step/page_%s.tif'%(i,))
                    img00=img.seek(i)

                except EOFError:
                    break
            del img

            try:
                img00.save('./output_step/SHOW1.png')


            except:
                pass

for par in [1,2,3,4]:
    os.system(f'rm -rf {pwd}/output_jpeg/')
    os.system(f'mkdir  {pwd}/output_jpeg/')
    for page in range(5000):

        macro=f'''open("/{pwd}/output_step/page_{page}.tif");
                        run("N2V predict", "modelfile={pwd}/n2v-{par}.bioimage.io.zip input=page_{page}.tif axes=XY batchsize=10 numtiles=1 showprogressdialog=true convertoutputtoinputformat=false");
                        saveAs("Tiff", "{pwd}/output_step/page_{page}.tif");
                       '''

        macro1 = f'''open("/{pwd}/output_step/page_{page}.tif");
                        run("N2V predict", "modelfile={pwd}/models/n2v-{par}.bioimage.io.zip input=page_{page}.tif axes=XY batchsize=10 numtiles=1 showprogressdialog=true convertoutputtoinputformat=false");
                        saveAs("JPEG", "{pwd}/output_jpeg/page_{page}.jpeg");
                       '''
        IJ.py.run_macro(macro)
        if page < 10:
            IJ.py.run_macro(macro1)
            # os.system(f'cp -rf {pwd}/output_jpeg/  /Users/macbookpro/Desktop/OneDrive/imagejresults/jpeg/jpeg{par}')
            print(page, end=',')
try:
    os.system(f'rm {pwd}/tiff_output/{tiff}')
except:
    pass
for sub in range(5000):
        macro_sub= f'''open("{pwd}/images_output_step/page_{sub}.tif");
                run("Subtract...", "value=60");
                saveAs("Tiff", "{pwd}/images_output_step/page_{sub}.tif"); '''
        IJ.py.run_macro(macro_sub)
import tifftools

input1 = tifftools.read_tiff(f'{pwd}/output_step/page_0.tif')

for i in range(1, 5000):
    input2 = tifftools.read_tiff(f'{pwd}/output_step/page_{i}.tif')
    # Add input2 to input1
    input1['ifds'].extend(input2['ifds'])
os.system(f'rm -rf {pwd}/tiff_output/')
os.system(f'mkdir {pwd}/tiff_output/')
tifftools.write_tiff(input1, f'{pwd}/tiff_output/output_N2V.tif')
# os.system(f'cp -rf {pwd}/tiff_output/  /Users/macbookpro/Desktop/OneDrive/imagejresults/output-n2v/output-n2v{par}')




