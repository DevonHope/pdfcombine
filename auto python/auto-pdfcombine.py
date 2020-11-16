import pip
import importlib
import os
from os import listdir, path
from os.path import isfile, join
from glob import glob  

def import_with_auto_install(package):
	try:
			return importlib.import_module(package)
	except ImportError:
			pip.main(['install', package])
	return importlib.import_module(package)
		
def autocombine(pypdf):
	cw = os.getcwd()
	list = glob(path.join(cw,"*.{}".format('pdf')))
	output = pypdf.PdfFileMerger()
	for file in list:
		pdf = pypdf.PdfFileReader(file)
		output.append(pdf)

	output.write("pdfcombine.pdf")


if __name__ == '__main__':
	pypdf = import_with_auto_install('PyPDF2')
	autocombine(pypdf)
    