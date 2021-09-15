# PDFCombine

## Description
The PDFCombine software can be used in three different ways as of right now. The headless python script simply combines all pdf files in the folder is it is in or a folder that is specified by the command line. The GUI python script can convert files from .pptx, .ppt, .doc, and .docx to .pdf and then combine them all into one PDF. The Latex file combines all listed PDF files into one Latex PDF.

- A Python script, headless
    - Combines all PDFs in a given folder.\
    __location:__ ```auto python/auto-pdfcombine.py```


- A Python script, GUI
    - Converts from any PowerPoint or Word Document file into PDF and combines them into one PDF.\
    __location:__ ```auto python/py2pdf-gui.py```


- A Latex script
    - Combines all PDFs listed in the file.\
    __location:__ ```non-auto tex/pdfCombine.tex```


## Use
### python
- __General purpose__: \
 ```python3 auto-pdfcombine.py```\
 or\
 ```py auto-pdfcombine.py```

- **Define path:**\
 ```python3 auto-pdfcombine.py /pdfs```\
 or \
 ```py auto-pdcombine.py /home/pdfs```

### latex
- __upating the latex file__\
change the file names in the latex file to the file names of the pdf files in the same dir as the latex file.

- __Run__\
Run the latex file in a latex ide or through a terminal
