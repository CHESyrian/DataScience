from dash import Dash, html, dash_table, dcc
import pandas as pd

# Incorporate data
df = pd.read_csv('Data/GOOG_1year.csv')

# Initialize the app
app = Dash()

# App layout Childreen
app_child = [
    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=20), 
    dcc.Graph(figure={}, id='controls-and-graph')
]

# App layout
app.layout = html.Div(children=app_child)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
