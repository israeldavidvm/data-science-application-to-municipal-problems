# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

def createListWithoutDuplicates(listWithDublicate):

    return list(set(listWithDublicate))

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])



df = pd.read_excel('proyecto/reports_TEST_min.xlsx')

provincias=sorted(createListWithoutDuplicates(df['Provincia']))


app = Dash(__name__)

app.layout = html.Div([
    html.H4(children='Proyecto de investiogacion de operaciones'),
    html.Br(),
        html.Label('Provincias'),
        dcc.Dropdown(provincias,
                     [],
                     multi=True),
    # generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)