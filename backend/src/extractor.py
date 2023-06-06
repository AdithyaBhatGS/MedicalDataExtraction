from pdf2image import convert_from_path

POPPLER_PATH=r'C:\poppler-23.01.0\Library\bin'

import pytesseract

import util 

from backend.src.prescription_parser import PrescriptionParser
from backend.src.patientDetails_parser import PatientDetailsParser

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract(file_path,file_format):
    
    #Converts the respective pdf to list of images (no of images depends on document)
    list_of_images=convert_from_path(file_path,poppler_path=POPPLER_PATH)

    # An empty string object
    document_text=''
    if len(list_of_images)>0:
        list_of_images=list_of_images[0]
        # util.preprocess_image(image)->Takes images as an argument and converts it into gray scale and then resizes it and applies adaptive thresolding and returns enhanced image
        preprocessedImage=util.preprocess_image(list_of_images)
        # extracting text from preprocessed image
        text=pytesseract.image_to_string(preprocessedImage,lang='eng')       
        # Add it to a string object
        document_text='\n'+text
    # We have 2 types of docs:

    if file_format=='patient_details':
        extracted_field_data=PatientDetailsParser(document_text).parse()
    elif file_format=='prescription':
        extracted_field_data = PrescriptionParser(document_text).parse()
    else:
        raise Exception(f'Invalid Document Format:{file_format}')
    return extracted_field_data
if __name__=='__main__':
    text=extract('../resources/patient_details/pd_2.pdf','patient_details')
    print(text)