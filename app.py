from dash import Dash, html, dcc 
import pandas as pd
import plotly.express as px

app = Dash()

df = pd.read_csv('pink_morsel_data.csv')

app.layout = html.Div(children=[
    html.H1(children='Visualization of Pink Morsel Sales'),

    html.Div(children='''
        The following graph shows the sales of pink morsel over time.
    '''),

    dcc.Graph(
        id='sales-graph',
        figure=px.line(df, x='date', y='sales')
    )
])

if __name__ == '__main__':
    app.run(debug=True)