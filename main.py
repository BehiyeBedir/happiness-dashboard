import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px


df = pd.read_csv("world-happiness-report-2021.csv")

app = dash.Dash(__name__)


fig = px.scatter(df, x="Logged GDP per capita", y="Ladder score",
                 hover_name="Country name",
                 color="Regional indicator",
                 title="Kişi Başı Gelir vs Mutluluk Skoru")

app.layout = html.Div([
    html.H1("Para İnsanı Mutlu Eder mi?"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)


