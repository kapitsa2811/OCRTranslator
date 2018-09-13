import argparse
import textwrap

from ocr.tesseractOCR import TesseractOCR
from translator.translatorInterface import TranslatorInterface

desc = "For more information, please visit: https://github.com/Nikolai10/OCR_Translator"

parser = argparse.ArgumentParser(
    prog='Format',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent('''\
         example calls:
             # german letter, to english translation
             python2.7 OCRTranslator_CL.py test.png de en --out_file out_en.txt
             
             # german letter, to russian translation
             python2.7 OCRTranslator_CL.py test.png de ru --out_file out_en.txt
         '''))

parser.description = desc
parser.add_argument("img", help="image")
parser.add_argument("in_lang", help="input language")
parser.add_argument("out_lang", help="output language")
parser.add_argument("--out_file", help="output file")

args = parser.parse_args()

print(args.img)

# OCR
ocr = TesseractOCR(args.img)
ocr_string = ocr.run_image_to_text()

# Translator
translator_de_en = TranslatorInterface(ocr_string, src_lang=args.in_lang, dest_lang=args.out_lang)
translation = translator_de_en.translate()

if args.out_file:
    translator_de_en.write_to_file(translation=translation, file_name=args.out_file)

print(translation)