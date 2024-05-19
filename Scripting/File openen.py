import csv #importeert csv

file = "kassa.csv" #dit is een variable om het makkelijker te maken om de bestandsnaam te gebruiken.

assortiment = [] #de list waar de gegevens in opgeslagen worden

# Openen en opslaan in assortiment van de gegevens in kassa.csv
with open(file, mode = 'r', newline='') as csvObject: #opend het bestand
    fileCSV = csv.reader(csvObject, delimiter=';') #zorgt ervoor dat het bestand goed uitgelezen wordt als een CSV bestand en geeft ";" aan als de scheiding
    header = next(fileCSV) #slaat de eerste regel op om te voorkomen dat we de header meenemen in de list
    for line in fileCSV: #slaat alle gegevens op in de list
        assortiment.append(line)