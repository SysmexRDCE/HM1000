import os
os.system('rm ./sub.ijm')
os.system('touch ./sub.ijm')

minus=(375-300)/1000
minus1=(300-200)/2000

value=375
for i in range(5000):

    if i<1000:
        value=value-minus
        macro=f'open("/Users/macbookpro/PycharmProjects/pyimagej/output_step3/page_{i}.tif"); run("Subtract Background...", "rolling=5"); run("Subtract...", "value={value}"); saveAs("Tiff", "/Users/macbookpro/PycharmProjects/pyimagej/output_step4/page_{i}.tif"); close(); '
        f = open('sub.ijm', 'a')

        f.write('\n' + macro)
        f.close()
    else:
        value=value-minus1
        macro = f'open("/Users/macbookpro/PycharmProjects/pyimagej/output_step3/page_{i}.tif"); run("Subtract Background...", "rolling=5"); run("Subtract...", "value={value}"); saveAs("Tiff", "/Users/macbookpro/PycharmProjects/pyimagej/output_step4/page_{i}.tif"); close(); '
        f = open('sub.ijm', 'a')

        f.write('\n' + macro)
        f.close()





