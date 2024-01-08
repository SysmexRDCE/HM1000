import ij.*;
import ij.process.*;
import ij.gui.*;
import java.awt.*;
import ij.plugin.*;

public class My_Plugin implements PlugIn {

	public void run(String arg) {
		IJ.run(imp, "N2V predict", "modelfile=/Users/macbookpro/PycharmProjects/pyimagej/models/n2v-1.bioimage.io.zip input=/Users/macbookpro/PycharmProjects/pyimagej/output_step/page_0.tif axes=XY batchsize=10 numtiles=1 showprogressdialog=true convertoutputtoinputformat=true");
		IJ.saveAs(imp, "Tiff", "/Users/macbookpro/PycharmProjects/pyimagej/output_step3/output0.tif");
		
	}

}
