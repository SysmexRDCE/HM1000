import os
try:
    os.system('rm ./thunderstorm.ijm')
except:
    pass
os.system('touch ./thunderstorm.ijm')

macro=f'''
open("/Users/macbookpro/PycharmProjects/pyimagej/tiff_output/488_opencv_sub.tif");
run("Camera setup", "offset=100.0 isemgain=false photons2adu=0.46 pixelsize=130.0");
run("Run analysis", "filter=[Wavelet filter (B-Spline)] scale=2.0 order=3 detector=[Local maximum] connectivity=8-neighbourhood threshold=std(Wave.F1) estimator=[PSF: Integrated Gaussian] sigma=1.6 fitradius=3 method=[Weighted Least squares] full_image_fitting=false mfaenabled=false renderer=[Normalized Gaussian] dxforce=false magnification=5.0 dx=20.0 colorizez=false threed=false dzforce=false repaint=50");
run("Export results", "filepath=/Users/macbookpro/PycharmProjects/pyimagej/csv_files/488_ThunderSTORM_results.csv fileformat=[CSV (comma separated)] sigma=true intensity=true chi2=true offset=true saveprotocol=true x=true y=true bkgstd=true id=true uncertainty=true frame=true");
selectWindow("Normalized Gaussian");
saveAs("Tiff", "/Users/macbookpro/PycharmProjects/pyimagej/sri_files/488_Normalized_Gaussian.tif");
'''
f = open('thunderstorm.ijm', 'a')
f.write('\n' + macro)
f.close()
macro=f'''
open("/Users/macbookpro/PycharmProjects/pyimagej/tiff_output/561_opencv_sub.tif");
run("Camera setup", "offset=100.0 isemgain=false photons2adu=0.46 pixelsize=130.0");
run("Run analysis", "filter=[Wavelet filter (B-Spline)] scale=2.0 order=3 detector=[Local maximum] connectivity=8-neighbourhood threshold=std(Wave.F1) estimator=[PSF: Integrated Gaussian] sigma=1.6 fitradius=3 method=[Weighted Least squares] full_image_fitting=false mfaenabled=false renderer=[Normalized Gaussian] dxforce=false magnification=5.0 dx=20.0 colorizez=false threed=false dzforce=false repaint=50");
run("Export results", "filepath=/Users/macbookpro/PycharmProjects/pyimagej/csv_files/561_ThunderSTORM_results.csv fileformat=[CSV (comma separated)] sigma=true intensity=true chi2=true offset=true saveprotocol=true x=true y=true bkgstd=true id=true uncertainty=true frame=true");
selectWindow("Normalized Gaussian");
saveAs("Tiff", "/Users/macbookpro/PycharmProjects/pyimagej/sri_files/561_Normalized_Gaussian.tif");
'''
f = open('thunderstorm.ijm', 'a')
f.write('\n' + macro)
f.close()