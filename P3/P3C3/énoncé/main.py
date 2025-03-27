import csv

# Ouvrir et lire le fichier input.csv
with open("input.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Préparer les données pour l'output
    data = []
    for row in reader:
        salaire = int(row["heures_travaillees"]) * 15  # Calcul du salaire
        data.append([row["nom"], row["heures_travaillees"], salaire])

# Écrire les données dans output.csv
with open("output.csv", mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["nom", "heures_travaillees", "salaire"])  # Écrire les en-têtes
    writer.writerows(data)  # Écrire les lignes de données

print("Le fichier output.csv a été créé avec succès.")
# Écrivez votre code ici !


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
