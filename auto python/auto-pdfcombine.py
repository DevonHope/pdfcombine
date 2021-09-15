#use:
#   py auto-pdfcombine.py <name of folder with files>
#	ex: py auto-pdfcombine.py lectures
#
#	or
#
#	put the py file in the folder of files to combine and use
# 	ex: py auto-pdfcombine.py
#

import pip
import importlib
import os
import sys
from os import listdir, path
from os.path import isfile, join
from glob import glob
# import ppt2pdf
import subprocess

# list of supported file types
lsf = ('*.pdf','*.pptx')

def import_with_auto_install(package):
	try:
			return importlib.import_module(package)
	except ImportError:
			pip.main(['install', package])
	return importlib.import_module(package)

# combine all pdfs in folder
def combine(cw, fn):
	list = glob(path.join(cw,"*.{}".format('pdf')))
	ln_list = len(list)

	if ln_list < 2:
		print(str(ln_list) + ' PDF files found in this directory...')

	else:
		output = pypdf.PdfFileMerger()

		for file in list:
			pdf = pypdf.PdfFileReader(file)
			output.append(pdf)

		output.write(fn)
		os.startfile(fn)

# convert supported file types to pdf
# uses LibreOffice
def convert(l,cdw, a2p):
	# libreoffice api
	# a2p_c = a2p.Api2Pdf('d3bed5ad-570a-4aa9-8f8d-d9057996afca')

	for f in l:
		if f[-4:] == 'pptx':
			of = cdw+"\\"+f
			# libreoffice
			cm = ['C:\Program Files\LibreOffice\program\soffice',
					'--headless', '--convert-to', 'pdf', of,'--outdir', cdw]
			print(cm)
			subprocess.run(cm)

			# LibreOffice api
			#api_res = a2p_c.LibreOffice.convert_from_url(of)
			#print(api_res['pdf'])

		#elif f[-3:] == 'pdf':

def autocombine(pypdf, cw):
	fn = "pdfcombine.pdf"
	fn = "\\".join((cw, fn))

	# get list of all files in folder
	list=[]
	for ext in lsf:
		list.extend(glob(path.join(cw,ext)))
	#print(list)

# convert from anything (pptx,..) to pdf

	# uses powerpoint, not headless
	cm = 'ppt2pdf dir '+ cw
	print(cm)
	subprocess.run(cm)

	# uses libreoffice
	#cdw = os.getcwd() + '\\'+cw
	#convert(list,cdw)

	# use api2pdf API libreoffice
	# convert(list,cdw,a2p)

	combine(cw, fn)

# determine if arguments are given
def work_dir():
	#print(len(sys.argv))
	if len(sys.argv) > 1:
		return sys.argv[1]
	else:
		print("No directory passed as arg...")
		print("Using current directory...")
		return os.getcwd()

if __name__ == '__main__':
	pypdf = import_with_auto_install('PyPDF2')
	import_with_auto_install('ppt2pdf')
	# apipdf = import_with_auto_install('api2pdf')

	# use api2pdf
	# a2pdf(apipdf, work_dir())

	autocombine(pypdf, work_dir())
