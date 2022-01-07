"""
Basic PDF to DOCX Converter.
Author: @akerdogmus
"""

import sys
from pdf2docx import Converter


class Pdf2DocxConverter():
    """
    PDF to DOCX Converter class
    """
    def __init__(self):
        self.pdf_file = sys.argv[1]
        self.docx_file = None

        if self.pdf_file == ("-h" or "--help"):
            self.help_section()
        else:
            self.pdf2docx_converter()

    def pdf2docx_converter(self):
        """Converter function"""

        print("Converting..")
        convert_file = Converter(self.pdf_file + ".pdf")
        self.docx_file = self.pdf_file + ".docx"
        convert_file.convert(self.docx_file)
        convert_file.close()
        print("Converted..")

    @classmethod
    def help_section(cls):
        """Help section function"""
        print("PDF to DOCX Converter. Use 'python3 pdf2docx_converter.py {pdf_name}'")

if __name__ == '__main__':
    try:
        Pdf2DocxConverter()
    except IndexError:
        print("PDF to DOCX Converter. For usage help, use 'python3 pdf2docx_converter.py -h'")
