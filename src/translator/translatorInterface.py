from googletrans import Translator
import logging


class TranslatorInterface:
    """
    this class uses google translate
    (https://www.codeproject.com/Tips/1236705/How-to-Use-Google-Translator-in-Python)

    Return value of translate API is a Translated class object, which has the following member variables.

    config:
    src - source language (default: auto)
    dest - destination language (default: en)
    origin - original text
    text - translated text
    pronunciation - pronunciation
    """
    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO)
    logger = logging.getLogger('Google Translate')

    def __init__(self, input_string, src_lang, dest_lang):
        """

        :param input_string:        string to translate
        """
        self.input_string = input_string
        self.translator = Translator() # Create object of Translator.
        self.src_lang = src_lang
        self.dest_lang = dest_lang

    def translate(self):
        self.logger.info('Current process: %s', 'translate...')
        return self.translator.translate(self.input_string, src=self.src_lang, dest=self.dest_lang).text

    def write_to_file(self, translation, file_name):
        """
        write translation so specified output_file

        :param translation:
        :param file_name:
        :return:
        """
        with open(file_name, 'w') as output_file:
            output_file.write(translation.encode('UTF-8'))

        return True