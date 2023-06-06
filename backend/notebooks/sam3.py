import re

text='''
Patient Medical Record . : :

Patient Information


Birth Date
Kathy Crawford May 6 1972
(737) 988-0851 Weight:
9264 Ash Dr 95
New York City, 10005 a
United States Height:
190
In Case of Emergency
ee oe
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
I i
Chicken Pox (Varicella): Measies:
IMMUNE IMMUNE
Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches):

Migraine'''


pattern='Patient Information(.*?)\(\d{3}\)'

name=re.findall(pattern, text,flags=re.DOTALL)

# print(matches)
# temp=matches[0].replace('Birth Date','').strip()

# pattern='May.*'
# matches=re.findall(pattern, temp)

# temp1=temp.replace(matches[0],'')
# print(temp1)

# remove_noise_from_name(name)
 
pattern='Patient Information.*?(\(\d{3}\) \d{3}-\d{4})'

phone_number=re.findall(pattern, text,flags=re.DOTALL)

print(phone_number)