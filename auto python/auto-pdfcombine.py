import pip
import importlib
import os
import sys
from os import listdir, path
from os.path import isfile, join
from glob import glob  

def import_with_auto_install(package):
	try:
			return importlib.import_module(package)
	except ImportError:
			pip.main(['install', package])
	return importlib.import_module(package)
		
def autocombine(pypdf, cw):
	fn = "pdfcombine.pdf"

	if cw is None: 
		cw = os.getcwd()
	else:
		fn = "\\".join((cw, fn))
	
	list = glob(path.join(cw,"*.{}".format('pdf')))
	output = pypdf.PdfFileMerger()
	
	for file in list:
		pdf = pypdf.PdfFileReader(file)
		output.append(pdf)

	output.write(fn)
	os.startfile(fn)


if __name__ == '__main__':
	pypdf = import_with_auto_install('PyPDF2')
	autocombine(pypdf, sys.argv[1])
    