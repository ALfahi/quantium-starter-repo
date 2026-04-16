from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent# points to our quantium folder, allows us to be OS independant
app = Dash()
data = pd.read_csv(BASE_DIR / "data" / "cleaned_data.csv")
data = data.sort_values(by=['date'])# we want to sort by date
lineChart = px.line(data, x='date', y='sales', 
                    labels={'date': 'Date', 'sales': 'Sales'},
                    title= "pink morsel sales data"
            )



COLOUR_MAP = {# we want to map regions to different colours
    "north": "blue",
    "south": "red",
    "east": "green",
    "west": "orange"
}

# function to handle users clicking the radio button and displaying different sets of data
@app.callback(
    Output('lineChart', 'figure'),
    Input('regionFilter', 'value')
)

def updatGraph(selected_region):

    if selected_region == 'all':
        filtered_df = data
    else:
        filtered_df = data[data['region'] == selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        color_discrete_map=COLOUR_MAP,# we want it to persist the colour even after user has clicked on a radio button
        color='region',
        labels={'date': 'Date', 'sales': 'Sales', 'region': 'Region'},
        title="Pink Morsel Sales Data"
    )

    return fig

app.layout = html.Div(children=[
    html.H2(children='Soul Foods Analytics', className="header"),

    dcc.RadioItems(
        id='regionFilter',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'South', 'value': 'south'},
            {'label': 'East', 'value': 'east'},
            {'label': 'West', 'value': 'west'},
        ],
        value='all',
        inline=True,
        className="radio"
    ),

    dcc.Graph(
        id='lineChart',
        figure=lineChart
    )
])


if __name__ == '__main__':
    app.run(debug=True)