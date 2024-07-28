from dash import Dash, dash_table
import pandas as pd

# Definition der Reihenfolgen
celestial_bodies = ["Kerbin", "Minmus", "Mun", "Duna", "Ike", "Dres", "Eve", "Gilly", "Eeloo", "Moho", "Jool", "Pol", "Bop", "Vall", "Tylo", "Laythe", "Sun"]
situations = ["SrfLanded", "SrfSplashed", "FlyingLow", "FlyingHigh", "InSpaceLow", "InSpaceHigh"]
situations_recovery = ["Landed", "Splashed", "Flew", "SubOrbited", "Orbited", "Flyby"]
experiments = ["surfaceSample", "evaReport", "crewReport", "mysteryGoo", "mobileMaterialsLab", "temperatureScan", "barometerScan", "gravityScan", "seismicScan", "athmosphereAnalysis", "evaScience", "infraredTelescope", "magnetometer", "asteroidSample", "cometSample", "recovery"]

def read_csv_files():
    # Einlesen der CSV-Dateien
    biomes_df = pd.read_csv('C:\\Users\\danie\\OneDrive\\Software\\KSP Science Checklist\\all biomes.csv')
    possible_combinations_df = pd.read_csv('C:\\Users\\danie\\OneDrive\\Software\\KSP Science Checklist\\possible combinations.csv')
    return biomes_df, possible_combinations_df

def create_table_data(biomes_df, possible_combinations_df):
    # Initialisieren der Datenstruktur für die Tabelle
    table_data = []

    # Durchlaufen der Planeten, Situationen und Biome
    for planet in celestial_bodies:
        for situation in situations:
            biomes = biomes_df[planet].dropna().tolist() if planet in biomes_df else []
            if not biomes:
                # Fall ohne Biome
                for experiment in experiments:
                    combination_exists = not possible_combinations_df[
                        (possible_combinations_df['Experiment'] == experiment) &
                        (possible_combinations_df['Planet'] == planet) &
                        (possible_combinations_df['Situation'] == situation)
                    ].empty
                    if combination_exists:
                        row = {"planet": planet, "situation": situation, "biome": ""}
                        row.update({exp: "" for exp in experiments})
                        table_data.append(row)
            else:
                # Fall mit Biomen
                for biome in biomes:
                    for experiment in experiments:
                        combination_exists = not possible_combinations_df[
                            (possible_combinations_df['Experiment'] == experiment) &
                            (possible_combinations_df['Planet'] == planet) &
                            (possible_combinations_df['Situation'] == situation) &
                            (possible_combinations_df['Biome'] == biome)
                        ].empty
                        if combination_exists:
                            row = {"planet": planet, "situation": situation, "biome": biome}
                            row.update({exp: "" for exp in experiments})
                            table_data.append(row)
    return table_data

def create_dash_app(table_data):
    # Erstellen der Dash App
    app = Dash(__name__)

    # Erstellen des Layouts
    app.layout = dash_table.DataTable(
        columns=[
            {"name": "", "id": "planet"},
            {"name": "", "id": "situation"},
            {"name": "", "id": "biome"},
            *[{"name": exp, "id": exp} for exp in experiments]
        ],
        data=table_data,
        merge_duplicate_headers=True,
        page_size=5000,  # Mit einem großen Wert die Paginierung verhindern
        style_header={'backgroundColor': '#305D91', 'color': '#FFFFFF'}
    )

    return app

def main():
    # Einlesen der CSV-Dateien
    biomes_df, possible_combinations_df = read_csv_files()

    # Erstellen der Tabellendaten
    table_data = create_table_data(biomes_df, possible_combinations_df)

    # Erstellen der Dash App
    app = create_dash_app(table_data)

    # Starten der Dash App
    app.run_server(debug=True)

if __name__ == '__main__':
    main()
