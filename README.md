# OCR Translator (Linux OS)
Keywords: `OCR`, `Tesseract-OCR`, `Google Translate`, `Shell Script`, `Linux` 

## 1. Introduction: OCR Translator

Immigrants often struggle to understand letters in a foreign language received by mail. 
OCR Translator aims to overcome language barriers, by using Tesseract-OCR and Google Translate. 

## 2. Workflow

<p align="center">
  <img width="70%" height="90%" src=docs/OCR_Translator.png>
</p>

**notice**: the preferred way is using a flatbed scanner, camera-based functionality will be added in future releases.

## 3. Config 
1. Install dependencies (using conda virtualenv)
```  
    # navigate to ./anaconda 
    conda env create --file environment.yml
    
    # activate OCR_Translator_env
    source activate OCR_Translator_env
```  

**Notes:**

- currently supported data types: PDF, png
- one page only (multiple pdf pages won't work)    
    
## 4. Resources

- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)
- [Google Translate](https://pypi.org/project/googletrans/)

## License

![OCR_Translator_license](LICENSE)
