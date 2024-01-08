import pickle
import os
pwd = os.getcwd()
pickle_in = open(f'{pwd}/selectedtiff.pkl', 'rb')
selectedtiff = pickle.load(pickle_in)


from os import listdir
from os.path import isfile, join
import imagej

IJ = imagej.init('/Applications/Fiji.app', headless=True)
macro3=f'''
open("{pwd}/tiff_output/output_N2V.tif");
run("Camera setup", "offset=100.0 isemgain=false photons2adu=0.46 pixelsize=130.0");
run("Run analysis", "filter=[Wavelet filter (B-Spline)] scale=2.0 order=3 detector=[Local maximum] connectivity=8-neighbourhood threshold=std(Wave.F1) estimator=[PSF: Integrated Gaussian] sigma=1.6 fitradius=3 method=[Weighted Least squares] full_image_fitting=false mfaenabled=false renderer=[Normalized Gaussian] dxforce=false magnification=5.0 dx=20.0 colorizez=false threed=false dzforce=false repaint=50");
selectWindow("Normalized Gaussian");
saveAs("Tiff", "{pwd}/sri_files/Normalized Gaussian.tif");
close();
run("Export results", "filepath={pwd}/csv_files/file.csv fileformat=[CSV (comma separated)] sigma=true intensity=true chi2=true offset=true saveprotocol=true x=true y=true bkgstd=true id=true uncertainty=true frame=true");
'''
IJ.py.run_macro(macro3)
