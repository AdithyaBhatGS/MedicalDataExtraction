from backend.src.parser_generic import MedicalParser

import re
class PrescriptionParser(MedicalParser):

    def __init__(self,text):
        MedicalParser.__init__(self,text)
    # parse()->returns the imporatant fields from the text extracted by ocr
    def parse(self):
        return {
            'patient_name':self.get_field_value('patient_name'),
            'patient_address':self.get_field_value('patient_address'),
            'medicines':self.get_field_value('medicines'),
            'directions':self.get_field_value('directions'),
            'refill':self.get_field_value('refill')
        } 
    # DOTALL()->'.' matches new line as well(if not specified it matches only that line)  
    def get_field_value(self,field_name):
        dict_of_field_info={
            'patient_name':{'pattern':'Name:(.*)Date','flags':0},
            'patient_address':{'pattern':'Address:(.*)\n','flags':0},
            'medicines':{'pattern':'Address[^\n]*(.*)Directions','flags':re.DOTALL},
            'directions':{'pattern':'Directions:(.*)Refill','flags':re.DOTALL},
            'refill':{'pattern':"Refill:(.*)times",'flags':0}
        }

        # 'patient_name':{'pattern':'Name:(.*)Date','flags':0}
            
        pattern_obj=dict_of_field_info.get(field_name,0)
        if pattern_obj:
            matches=re.findall(pattern_obj['pattern'],self.text,flags=pattern_obj['flags'])
            # matches will return list of strings
            if len(matches)>0:
                return matches[0].strip()
    
if __name__=='__main__':
    documentText='''Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times'''
    documentText2='''Dr John >mith, M.D

2 Non-Important street,
New York, Phone (900)-323- ~2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

| Omeprazole 40 mg

Directions: Use two tablets daily for three months

Refill: 3 times
    '''
    p=PrescriptionParser(documentText)
    print(p.parse())