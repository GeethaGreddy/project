changingParam = ['Gender','Chest_Pain_Type','Fasting_BS','Resting_ECG','ST_Slope','Family_History','Exercise_Angina']
changingValues = [['Female','Male'],['','ASY','ATA','NAP'],['Less than 120 mg/dL','More than 120 mg/dL'],['','LVH','Normal','ST'],['','Down','Flat','Up'],['No CHD present in family','CHD was present in family'],['No','Yes']]


def generateProfile(data):
    Person_Profile = []
    for x in data:
        if x in changingParam:
            X_index = changingParam.index(x)
            newStrings = x.replace('_'," ") + '  :  ' + changingValues[X_index][int(data[x])]
        else:
            newStrings = x.replace('_'," ") + '  :  ' + data[x]
        Person_Profile.append(newStrings)
    print(Person_Profile)
    return Person_Profile

def generateOutput(prediction):
    base = 'From the given profile our model has predicted : '
    choice = ['The person does not have Cardio Vascular Disease(CVD)','The person does have Cardio Vascular Disease(CVD)']
    
    return base + choice[prediction]