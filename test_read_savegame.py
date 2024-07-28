import re
import pandas as pd

# Savegame auslesen und Science-Werte übernehmen
# Definiere den Pfad zur Datei
eingabepfad = r'C:\Games\Kerbal Space Program\saves\letzter Neustart\persistent.sfs'

# Lese den Inhalt der Datei und speichere ihn in einer Variablen
with open(eingabepfad, 'r', encoding='utf-8') as datei:
    savegame_inhalt = datei.read()

# Suche nach dem Beginn der Science-Einträge
suchbegriff = r"\t\tScience\s*\{\s*id\s*=\s*"
match = re.search(suchbegriff, savegame_inhalt, re.MULTILINE)

# Finde den Index des ersten Vorkommens des Suchbegriffs
start_index = match.start()
# Lösche alles vor dem Suchbegriff
savegame_inhalt = savegame_inhalt[start_index:]
print(f"Suchbegriff '{suchbegriff}' gefunden und Inhalt davor gelöscht.")

# Suche nach dem Ende der Science-Einträge
pattern = r'\}\s*(?!\s*Science)'
match = re.search(pattern, savegame_inhalt, re.DOTALL)

# Finde den Index des ersten Vorkommens des }
end_index = match.start()
# Lösche alles nach dem }
savegame_inhalt = savegame_inhalt[:end_index + 1]

# Extrahiere alle Science-Einträge
science_entries = re.findall(
    r'Science\s*\{\s*id\s*=\s*(.*?)\s*title\s*=\s*(.*?)\s*dsc\s*=\s*(.*?)\s*scv\s*=\s*(.*?)\s*sbv\s*=\s*(.*?)\s*sci\s*=\s*(.*?)\s*asc\s*=\s*(.*?)\s*cap\s*=\s*(.*?)\s*\}', 
    savegame_inhalt, 
    re.DOTALL
)

# Erstelle ein DataFrame aus den extrahierten Science-Einträgen
df = pd.DataFrame(science_entries, columns=[
    'id', 'title', 'dsc', 'scv', 'sbv', 'sci', 'asc', 'cap'
])

# Überprüfe, ob die 'id'-Spalte existiert und bereinige die Spaltennamen
df.columns = df.columns.str.strip()

# Lösche alle Zeilen, in denen der Wert für 'sci' gleich "0" ist
df = df[df['sci'] != "0"]

# CSV-Datei einlesen, die alle möglichen Science-IDs enthält
csv_pfad = r'C:\Users\danie\OneDrive\Software\KSP Science Checklist\possible combinations.csv'
possible_combinations_df = pd.read_csv(csv_pfad, delimiter=';')  # Stelle sicher, dass der korrekte Delimiter verwendet wird

# Überprüfe, ob die 'id'-Spalte in possible_combinations_df existiert und bereinige die Spaltennamen
possible_combinations_df.columns = possible_combinations_df.columns.str.strip()

# Merge der beiden DataFrames, wobei nur die übereinstimmenden IDs beibehalten werden
merged_df = df.merge(possible_combinations_df, on='id', how='inner')

# Finde die IDs, die im ursprünglichen DataFrame 'df' aber nicht im 'merged_df' sind
missing_ids = df[~df['id'].isin(merged_df['id'])]
ausgabepfad = r'C:\Users\danie\OneDrive\Software\KSP Science Checklist\missing_ids.csv'
missing_ids.to_csv(ausgabepfad, sep=';', index=False)


# Ausgabe der Zeilen, die nicht gematcht wurden
print("Zeilen, die nicht gematcht wurden:")
print(missing_ids)

# Ausgabe des resultierenden DataFrames zur Überprüfung
print("Resultierendes DataFrame nach dem Merge:")
print(merged_df)
