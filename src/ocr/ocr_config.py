"""prototype config"""

# shared props
python_v = 'python2.7'

class TesseractOCRConfig:
    psm = '--psm 3'             # Fully automatic page segmentation, but no OSD. (Default)
    oem = '--oem 1'             # LSTM-based recognition