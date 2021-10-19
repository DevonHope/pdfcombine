# py2pdf-gui.py

import PySimpleGUI as sg
import pip
import importlib
import sys
from os import listdir, startfile, system
from os.path import isfile, join, splitext, exists
from glob import glob
import win32com.client
import subprocess
import time
# from docx2pdf import convert as dcon
# from PyPDF2 import PdfFileMerger, PdfFileReader
# from ppt2pdf.main import convert as pcon

ftypes = ['All','Custom']
# ,'.pptx', '.docx'
supported_ftypes = ('.pdf','.pdf')
dont_show = False
log_txt = 'opened = True'

# Left side of app

file_list_column = [
    [
        sg.Text("File Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-",
            select_mode='multiple'
        ),
    ],
    [
        sg.Button('Add Selected Items', key='-ADD-')
    ],
    [
        sg.Button("Select Only", key='-SELECT-'),
        sg.OptionMenu(values=ftypes,default_value=ftypes[0],size=(4,8), key='-FT-'),
    ],
]

# Right side of app

selected_list_col = [
    [
        sg.Text('Items to convert and combine'),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20), key='-SELLIST-',
            select_mode='multiple'
        ),
    ],
    [
        sg.Button('Remove Selected Items',key='-REMOVE-')
    ],
    [
        sg.Text('Combined PDF file name:'),
    ],
    [
        sg.In(size=(25,1),enable_events=True,key="-FN-"),
        sg.Button("Convert & Combine", key='-CC-'),
    ],
]

# ----- Full layout -----
first_col = sg.Column(file_list_column)

layout = [
    [
        first_col,
        sg.VSeperator(),
        sg.Column(selected_list_col),
    ]
]

def import_with_auto_install(package):
	try:
			return importlib.import_module(package)
	except ImportError:
			pip.main(['install', package])
	return importlib.import_module(package)

# combine all pdfs in folder
def combine(files, fn, pypdf):
    ln_list = len(files)

    if ln_list < 2:
        print(str(ln_list) + ' PDF files found in this directory...')
    else:
        output = pypdf.PdfFileMerger()

        for file in files:
            print("Filename: "+file)
            try:
                pdf = pypdf.PdfFileReader(file)
                output.append(pdf)
            except:
                sg.Popup('File was not converted', keep_on_top=True)

        output.write(fn)
        startfile(fn)

def autocombine(cw, fn, files, docx, ppt, pypdf):
    if len(fn) < 1:
	       fn = "pdfcombine.pdf"
    fn = "\\".join((cw, fn))
    new_f = []
    # convert from anything (pptx,..) to pdf
    for f in files:
        f = "\\".join((cw, f))
        if f[-4:] == 'pptx':
            fi = f.replace('pptx','pdf')
            ppt.main.convert(f,fi)
            new_f.append(fi)
        elif f[-4:] == 'docx':
            fi = f.replace('docx','pdf')
            docx.convert(f,fi)
            new_f.append(fi)
        elif f[-3:] == 'pdf':
            new_f.append(f)

    #pptpdf(ppt)
    combine(new_f, fn, pypdf)

def launch(pypdf, ppt, docx):
    # Create the window
    window = sg.Window("Py2PDF Combine", layout)
    sg.Popup('MS Powerpoint and Word (.pptx, .ppt, .doc, .docx) file do not work as of right now.', keep_on_top=True)
    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
         # Folder name was filled in, make a list of files in the folder

        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                # Get list of files in folder
                file_list = listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if isfile(join(folder, f))
                and f.lower().endswith(supported_ftypes)
            ]

            ftype_update=ftypes
            # loop through supported file formats
            for sft in supported_ftypes:
                sft = sft.split('.')[1]
                for fn in fnames:
                    ft = fn[-len(sft):]
                    if ft == sft:
                        if not ft in ftype_update:
                            ftype_update.append(ft)

            window["-FILE LIST-"].update(fnames)
            window['-FT-'].update(values=ftype_update)

        # select button event
        if event == "-SELECT-":
            select = values['-FT-']
            selected_items = []

            if select == 'All':
                selected_items = fnames
            elif select == 'Custom':
                selected_items = window['-FILE LIST-'].get()
            else:
                # loop through listbox list and find selected ext items
                for sft in supported_ftypes:
                    if select == sft.split('.')[1]:
                        sft = sft.split('.')[1]
                        for f in fnames:
                            if f[-len(sft):] == sft:
                                selected_items.append(f)

            window['-SELLIST-'].update(values=selected_items)
            #sg.Popup('Selected ', values['-FILE LIST-'])

        # append selected items
        if event == '-ADD-':
            select = window['-FILE LIST-'].get()
            cur_selection = window['-SELLIST-'].get_list_values()

            # if selected items are already in list dont extend
            window['-SELLIST-'].update(values=list(set(select + cur_selection)))

        # Remove selected items function
        if event == '-REMOVE-':
            get_vl = window['-SELLIST-'].get_list_values()
            si = window['-SELLIST-'].get()
            vl = [f for f in get_vl if f not in si]
            window['-SELLIST-'].update(values=vl)

        if event == '-CC-':
            # get name of file to save too
            if values['-FN-']:
                fn = values['-FN-']
                fn = fn +'.pdf'
            else:
                fn = 'pdfcombine.pdf'

            # get list of files
            dir = window['-FOLDER-'].get()
            files = window['-SELLIST-'].get_list_values()
            autocombine(dir, fn, files, docx, ppt, pypdf)

    window.close()

if __name__ == '__main__':

    # FOR LINUX
    #import_with_auto_install('unoconv')

    pypdf = import_with_auto_install('PyPDF2')
    ppt = import_with_auto_install('ppt2pdf')
    docx = import_with_auto_install('docx2pdf')

    launch(pypdf, ppt, docx)
