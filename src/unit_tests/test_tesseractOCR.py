from unittest import TestCase
from ocr.tesseractOCR import TesseractOCR


class TestTesseractOCR(TestCase):
    img_name = '../../resources_private/test1.pdf'

    def test_image_to_text(self):
        ocr = TesseractOCR(self.img_name, 'de')
        print(ocr.run_image_to_text())