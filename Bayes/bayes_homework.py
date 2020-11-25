import numpy as np
import pandas as pd

disease = pd.read_csv(r'disease.csv', sep=';')
symptom = pd.read_csv(r'symptom.csv', sep=';')

testData = [np.random.randint(2) for i in range(len(symptom) - 1)]
print(testData)

patientsCountTable = disease['количество пациентов'].to_numpy()
totalPatientsCount = patientsCountTable[len(patientsCountTable) - 1]
proportionsToTotalCount = [patientsCountTable[i] / totalPatientsCount for i in range(len(patientsCountTable) - 1)]

illnessColumn = disease['Болезнь']
illnessNames = illnessColumn.head(len(illnessColumn) - 1)
illnessProbability = [1 for i in range(0, len(illnessNames))]
for i in range(len(illnessNames)):
    illnessProbability[i] *= proportionsToTotalCount[i]
    for j in range(len(symptom) - 1):
        if testData[j] == 1:
            illnessProbability[i] *= float(symptom.iloc[j][i + 1].replace(',', '.'))

mostPossibleDiseaseIndex = illnessProbability.index(max(illnessProbability))
verdict = disease['Болезнь'][mostPossibleDiseaseIndex]
print(verdict)
