import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import random

# Anzahl der Spalten und Zeilen
num_columns = 5
num_rows = 5

# Dummy-Daten erzeugen
data = {
    f"Spalte {i + 1}": [f"Zeile {j + 1}" for j in range(num_rows)]
    for i in range(num_columns)
}
df = pd.DataFrame(data)

# Initialisiere die Dash-Anwendung
app = dash.Dash(__name__)

# Definiere das Layout der Anwendung
app.layout = html.Div([
    html.H1("Dynamische Tabelle"),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'width': '100%', 'overflowX': 'auto'},
        style_cell={'textAlign': 'center'},
        style_header={
            'backgroundColor': 'grey',
            'fontWeight': 'bold'
        },
        style_data_conditional=[]
    ),
    dcc.Interval(
        id='interval-component',
        interval=10*1000,  # in Millisekunden (hier 10 Sekunden)
        n_intervals=0
    )
])

# Callback zur Aktualisierung der Zellenfarbe
@app.callback(
    Output('table', 'style_data_conditional'),
    Input('interval-component', 'n_intervals')
)
def update_cell_color(n):
    # Zufällige Farbe erzeugen
    random_color = f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'
    return [
        {
            'if': {
                'row_index': 1,  # Zeile 2 (0-basierter Index)
                'column_id': 'Spalte 2'  # Spalte 2
            },
            'backgroundColor': random_color
        }
    ]

if __name__ == '__main__':
    app.run_server(debug=True)
