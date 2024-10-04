student_profile = {
'24BCE0001':['HARSHINI KAILASAM', 'SCOPE', 'BCE'],
'24BCE0002':['ABEN BOBY THARAKAN', 'SMEC', 'BME'],
'24BCE0003':['AJAY KUMARAN P', 'SCOPE', 'BCE'],
'24BCE0004':['MANAS AGARWAL', 'SCOPE', 'BCE']
}

for key, value in student_profile.items():
    if key == '24BCE0004':
        print(f"The programme of {value[0]} is {value[2]}")