"""
Basic PDF to DOCX Converter.
Author: @akerdogmus
"""

from optparse import OptionParser
from pdf2docx import Converter


class Pdf2DocxConverter():
    """
    PDF to DOCX Converter class
    """
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file
        self.docx_file = None

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
    def option_parsing(cls):
        """Option Parser function, takes parameters from the user"""
        parse_object = OptionParser()
        parse_object.add_option("-f", "--file", dest = "pdf_file_name",
         help = "PDF file name for converting to docx.")
        (user_input, arguments) = parse_object.parse_args()
        return user_input.pdf_file_name, arguments

if __name__ == '__main__':
    try:
        option, args = Pdf2DocxConverter.option_parsing()
        Pdf2DocxConverter(option)

    except IndexError:
        print("PDF to DOCX Converter. For usage help, use 'python3 pdf2docx_converter.py -h'")
