import cv2
import pytesseract
import os
from pdf2image import convert_from_path
from ocr.ocr_config import *
import logging


class TesseractOCR:
    """
    this class uses the text line recognition module provided by
        - tesseract-ocr (https://github.com/tesseract-ocr/tesseract)
    using the pythonic wrapper
        - pytesseract (https://pypi.org/project/pytesseract/)

    tesseract version: 4.0.0-beta.1-372-g87635 (LSTM version)
    tesseract config:

    --psm N
           Set Tesseract to only run a subset of layout analysis and assume a certain form of image. The options for N are:

               0 = Orientation and script detection (OSD) only.
               1 = Automatic page segmentation with OSD.
               2 = Automatic page segmentation, but no OSD, or OCR.
               3 = Fully automatic page segmentation, but no OSD. (Default)
               4 = Assume a single column of text of variable sizes.
               5 = Assume a single uniform block of vertically aligned text.
               6 = Assume a single uniform block of text.
               7 = Treat the image as a single text line.
               8 = Treat the image as a single word.
               9 = Treat the image as a single word in a circle.
               10 = Treat the image as a single character.

       --oem N
           Specify OCR Engine mode. The options for N are:

               0 = Original Tesseract only.
               1 = Neural nets LSTM only.
               2 = Tesseract + LSTM.
               3 = Default, based on what is available.

    for more information, please check the manual provided by tesseract (cmd tool)
    """

    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO)
    logger = logging.getLogger('Tesseract-OCR')


    def __init__(self, img_name, lang='deu+eng'):
        """
        set tesseract-ocr config

        :param input_dir        dir of retrieved text line (images)
        :param config:          tesseract config
        :param lang:            language
        """
        self.toc = TesseractOCRConfig
        self.img_name = img_name

        # small hack
        if lang == 'de':
            lang = 'deu'

        # tesseract vars
        self.lang = lang
        self.oem = self.toc.oem
        self.psm = self.toc.psm

    def run_image_to_text(self):
        """apply ocr on entire image"""

        if self.pdf_to_png():
            self.logger.info('Current process: %s', 'Convert PDF to png')

        img = cv2.imread(self.img_png())
        ocr_result = pytesseract.image_to_string(img, lang=self.lang, config=self.oem + ' ' + self.psm)
        self.logger.info('Current process: %s', 'OCR')
        return ocr_result

    def pdf_to_png(self):
        """pdf to image"""
        file_name, ext = os.path.splitext(self.img_name)
        if ext.lower() == '.pdf':
            # convert to png and wright back to folder
            img_out = convert_from_path(self.img_name, thread_count=4)
            img_out[0].save(self.img_png(), 'png')
            return True
        return False

    def img_png(self):
        """return new name (with png ext)"""
        file_name, ext = os.path.splitext(self.img_name)
        return file_name + '.png'
