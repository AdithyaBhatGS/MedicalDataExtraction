from backend.src.prescription_parser import PrescriptionParser
import pytest

@pytest.fixture
def sharapova():
    text='''
Dr John Smith, M.D
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
    return PrescriptionParser(text)

@pytest.fixture
def virat():
    text='''
    Dr John Smith, M.D

    2 Non-Important street,
    New York, Phone (900)-323- ~2222

    Name:  Virat Kohli Date: 2/05/2022

    Address: 2 cricket blvd, New Delhi

    Omeprazole 40 mg

    Directions: Use two tablets daily for three months

    Refill: 3 times
    '''
    return PrescriptionParser(text)

def test_get_patient_name(sharapova,virat):

    # sharapova will be replaced by PrescriptionParser(text)

    assert sharapova.get_field_value('patient_name') == 'Marta Sharapova'
    assert virat.get_field_value('patient_name') == 'Virat Kohli'
    
def test_get_patient_address(sharapova,virat):
    assert sharapova.get_field_value('patient_address') == '9 tennis court, new Russia, DC'
    assert virat.get_field_value('patient_address') == '2 cricket blvd, New Delhi'

def test_get_medicines(sharapova,virat):
    assert sharapova.get_field_value('medicines') == 'Prednisone 20 mg\nLialda 2.4 gram'
    assert virat.get_field_value('medicines') == 'Omeprazole 40 mg'

def test_get_directions(sharapova,virat):
    assert sharapova.get_field_value('directions') == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month'
    assert virat.get_field_value('directions') == 'Use two tablets daily for three months'

def test_get_refill(sharapova,virat):
    assert sharapova.get_field_value('refill') == '2'
    assert virat.get_field_value('refill') == '3'

def test_parse(sharapova,virat):
    sharapova_dict=sharapova.parse()
    assert sharapova_dict == {
        'patient_name':'Marta Sharapova',
        'patient_address':'9 tennis court, new Russia, DC',
        'medicines':'Prednisone 20 mg\nLialda 2.4 gram',
        'directions':'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month',
        'refill':'2'
    }

    virat_dict=virat.parse()
    assert virat_dict == {
        'patient_name': 'Virat Kohli',
        'patient_address': '2 cricket blvd, New Delhi',
        'medicines': 'Omeprazole 40 mg',
        'directions': 'Use two tablets daily for three months',
        'refill': '3'
    }