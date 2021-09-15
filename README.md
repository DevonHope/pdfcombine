# PDFCombine

## Description
There are three different forms of PDFCombine. The headless python script simply converts all PowerPoint files and combines the pdf files in the folder is in or a folder that is specified by the command line. The GUI python script can convert files from .pptx, .ppt, .doc, and .docx to .pdf and then combine them all into one PDF. The Latex file combines all listed PDF files into one Latex PDF.

- A Python script, headless
    - Converts all PowerPoint files and combines the PDFs in a given folder.\
    __location:__ ```auto python/auto-pdfcombine.py```


- A Python script, GUI
    - Converts from any PowerPoint or Word Document file into PDF and combines them into one PDF.\
    __location:__ ```auto python/py2pdf-gui.py```


- A Latex script
    - Combines all PDFs listed in the file.\
    __location:__ ```non-auto tex/pdfCombine.tex```


## Use

### Python Headless
Requires Python3
- If Python file is placed in folder with files to convert/combine:\
    ```python3 auto-pdfcombine.py```\
    or\
    ```py auto-pdfcombine.py```

- If path is defined:\
    ```python3 auto-pdfcombine.py /pdfs```\
    or\
    ```py auto-pdcombine.py /home/pdfs```

### Python GUI
Requires Python3

```py py2pdf-gui.py```

### latex
- __upating the latex file__\
Change the file names in the latex file to the file names of the pdf files in the same dir as the latex file.

- __Run__\
Run the latex file in a latex ide or through a terminal
