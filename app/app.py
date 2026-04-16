from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent# points to our quantium folder, allows us to be OS independant
app = Dash()
data = pd.read_csv(BASE_DIR / "data" / "cleaned_data.csv")
data = data.sort_values(by=['date'])# we want to sort by date
lineChart = px.line(data, x='date', y='sales', 
                    labels={'date': 'Date', 'sales': 'Sales'}
            )

app.layout = html.Div(children=[
    html.H2(children='Line graph displaying the sales of pink morsels over time', className="header"),

    dcc.Graph(
        id='lineChart',
        figure=lineChart
    )
])


if __name__ == '__main__':
    app.run(debug=True)