from unittest import TestCase
from ocr.tesseractOCR import TesseractOCR
from translator.translatorInterface import TranslatorInterface


class TestTranslatorInterface(TestCase):
    #img_name = '../../resources_private/test1.pdf'
    img_name = '../../resources_private/img-180912231203-0001.pdf'

    def test_translate(self):

        src_lang = 'de'
        dest_lang_en = 'en'
        dest_lang_ru = 'ru'

        # retrieve content retrieved by tesseract OCR
        ocr = TesseractOCR(self.img_name, src_lang)
        ocr_string = ocr.run_image_to_text()

        print('=' * 80)
        print('OCR with tesseract 4.0.0 (LSTM-based)')
        print('=' * 80)
        print(ocr_string)
        print()

        translator_de_en = TranslatorInterface(ocr_string, src_lang=src_lang, dest_lang=dest_lang_en)
        translator_de_ru = TranslatorInterface(ocr_string, src_lang=src_lang, dest_lang=dest_lang_ru)

        print('=' * 80)
        print('Translate to english...')
        print('=' * 80)
        print()
        print(translator_de_en.translate())
        print()

        print('=' * 80)
        print('Translate to russian...')
        print('=' * 80)
        print()
        print(translator_de_ru.translate())
        print()