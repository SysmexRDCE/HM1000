import os


for i in range(4030,4300):
    macro=f'run("N2V predict", "modelfile=/Users/macbookpro/PycharmProjects/pyimagej/models/n2v-1.bioimage.io.zip input=/Users/macbookpro/PycharmProjects/pyimagej/output_step/page_{i}.tif axes=XY batchsize=10 numtiles=1 showprogressdialog=true convertoutputtoinputformat=true"); selectWindow("output"); saveAs("Tiff", "/Users/macbookpro/PycharmProjects/pyimagej/output_step3/page_{i}.tif"); close(); '
    f = open('4030.ijm', 'a')
    f.write('\n' + macro)
    f.close()
